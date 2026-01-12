import uuid
from datetime import datetime, timezone
from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import random

# Убедитесь, что URL вашей базы данных верный
DATABASE_URL = "postgresql+psycopg2://postgres:pass123@0.0.0.0:5432/forum"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
fake = Faker("ru_RU")


def now_utc():
    """Возвращает текущее время в UTC."""
    return datetime.now(timezone.utc)


def init_db():
    """Заполняет базу данных фейковыми данными."""
    session = SessionLocal()

    print("🚀 Начинаем заполнение базы данных...")

    # === USERS ===
    users_data = []
    for _ in range(10):
        users_data.append(
            {
                "sid": str(uuid.uuid4()),
                "username": fake.unique.user_name(),
                "email": fake.unique.email(),
                "password_hash": fake.sha256(),
                "role": random.choice(["user", "moderator", "admin"]),
                "is_banned": False,
                "created_at": now_utc(),
                "updated_at": now_utc(),
            }
        )
    for u in users_data:
        session.execute(
            text(
                """
                INSERT INTO users.users (sid, username, email, password_hash, role, is_banned, created_at, updated_at)
                VALUES (:sid, :username, :email, :password_hash, :role, :is_banned, :created_at, :updated_at)
                """
            ),
            u,
        )
    print(f"✅ Users: {len(users_data)} added")

    # === BOARD CATEGORIES ===
    board_categories_data = []
    for _ in range(3):
        board_categories_data.append(
            {
                "sid": str(uuid.uuid4()),
                "title": fake.word().capitalize(),
                "created_at": now_utc(),
                "updated_at": now_utc(),
            }
        )
    for bc in board_categories_data:
        session.execute(
            text(
                """
                INSERT INTO boards.board_categories (sid, title, created_at, updated_at)
                VALUES (:sid, :title, :created_at, :updated_at)
                """
            ),
            bc,
        )
    print(f"✅ Board Categories: {len(board_categories_data)} added")

    # === BOARDS ===
    boards_data = []
    for _ in range(5):
        boards_data.append(
            {
                "sid": str(uuid.uuid4()),
                "name": fake.unique.word()[:20],
                "description": fake.sentence(),
                "board_category_sid": random.choice(board_categories_data)["sid"],
                "created_at": now_utc(),
                "updated_at": now_utc(),
            }
        )
    for b in boards_data:
        session.execute(
            text(
                """
                INSERT INTO boards.boards (sid, name, description, board_category_sid, created_at, updated_at)
                VALUES (:sid, :name, :description, :board_category_sid, :created_at, :updated_at)
                """
            ),
            b,
        )
    print(f"✅ Boards: {len(boards_data)} added")

    # === THREADS ===
    threads_data = []
    for _ in range(10):
        threads_data.append(
            {
                "sid": str(uuid.uuid4()),
                "title": fake.sentence(nb_words=4),
                "is_locked": random.choice([True, False]),
                "is_pinned": random.choice([True, False]),
                "board_sid": random.choice(boards_data)["sid"],
                "user_sid": random.choice(users_data)["sid"],
                "created_at": now_utc(),
                "updated_at": now_utc(),
            }
        )
    for t in threads_data:
        session.execute(
            text(
                """
                INSERT INTO threads.threads (sid, title, is_locked, is_pinned, board_sid, user_sid, created_at, updated_at)
                VALUES (:sid, :title, :is_locked, :is_pinned, :board_sid, :user_sid, :created_at, :updated_at)
                """
            ),
            t,
        )
    print(f"✅ Threads: {len(threads_data)} added")

    # === POSTS (Подготовка) ===
    posts_data = []
    post_sids = []  # Для удобного выбора при генерации голосов

    for _ in range(30):
        p_sid = str(uuid.uuid4())
        post_sids.append(p_sid)
        posts_data.append(
            {
                "sid": p_sid,
                "content": fake.text(max_nb_chars=200),
                "thread_sid": random.choice(threads_data)["sid"],
                "user_sid": random.choice(users_data)["sid"],
                "score": 0,  # Пока 0, обновим позже
                "created_at": now_utc(),
                "updated_at": now_utc(),
            }
        )

    # === POST_VOTES (Генерация и подсчет Score) ===
    votes_data = []
    created_votes = set()

    # Словарь для подсчета рейтинга: {post_sid: score}
    post_scores = {p["sid"]: 0 for p in posts_data}

    for _ in range(100):  # Делаем больше голосов, чтобы рейтинг был интересным
        user_sid = random.choice(users_data)["sid"]
        post_sid = random.choice(post_sids)

        if (user_sid, post_sid) not in created_votes:
            value = random.choice([-1, 1])
            votes_data.append(
                {
                    "sid": str(uuid.uuid4()),
                    "post_sid": post_sid,
                    "user_sid": user_sid,
                    "value": value,
                    "created_at": now_utc(),
                    "updated_at": now_utc(),
                }
            )
            created_votes.add((user_sid, post_sid))
            # Обновляем счетчик
            post_scores[post_sid] += value

    # === INSERT POSTS (уже с правильным score) ===
    for p in posts_data:
        # Присваиваем посчитанный рейтинг
        p["score"] = post_scores[p["sid"]]

        session.execute(
            text(
                """
                INSERT INTO posts.posts (sid, content, score, thread_sid, user_sid, created_at, updated_at)
                VALUES (:sid, :content, :score, :thread_sid, :user_sid, :created_at, :updated_at)
                """
            ),
            p,
        )
    print(f"✅ Posts: {len(posts_data)} added (with calculated scores)")

    # === INSERT VOTES ===
    for v in votes_data:
        session.execute(
            text(
                """
                INSERT INTO post_votes.post_votes (sid, post_sid, user_sid, value, created_at, updated_at)
                VALUES (:sid, :post_sid, :user_sid, :value, :created_at, :updated_at)
                """
            ),
            v,
        )
    print(f"✅ Votes: {len(votes_data)} added")

    session.commit()
    session.close()
    print("🎉 База данных успешно заполнена!")


if __name__ == "__main__":
    init_db()
