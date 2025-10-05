import uuid
from datetime import datetime, UTC
from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import random

# ✅ строка подключения — как строка, а не кортеж
DATABASE_URL = "postgresql+psycopg2://postgres:pass123@0.0.0.0:5432/forum"

# создаём движок и сессию
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
fake = Faker("ru_RU")


def init_db():
    session = SessionLocal()

    # ==== USERS ====
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
                "created_at": datetime.now(UTC),
                "updated_at": datetime.now(UTC),
            }
        )

    for u in users_data:
        session.execute(
            text("""
                INSERT INTO users.users (sid, username, email, password_hash, role, is_banned, created_at, updated_at)
                VALUES (:sid, :username, :email, :password_hash, :role, :is_banned, :created_at, :updated_at)
            """),
            u,
        )

    # ==== BOARDS ====
    boards_data = []
    for _ in range(5):
        boards_data.append(
            {
                "sid": str(uuid.uuid4()),
                "name": fake.unique.word()[:20],
                "description": fake.sentence(),
                "created_at": datetime.now(UTC),
                "updated_at": datetime.now(UTC),
            }
        )

    for b in boards_data:
        session.execute(
            text("""
                INSERT INTO boards.boards (sid, name, description, created_at, updated_at)
                VALUES (:sid, :name, :description, :created_at, :updated_at)
            """),
            b,
        )

    # ==== THREADS ====
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
                "created_at": datetime.now(UTC),
                "updated_at": datetime.now(UTC),
            }
        )

    for t in threads_data:
        session.execute(
            text("""
                INSERT INTO threads.threads (sid, title, is_locked, is_pinned, board_sid, user_sid, created_at, updated_at)
                VALUES (:sid, :title, :is_locked, :is_pinned, :board_sid, :user_sid, :created_at, :updated_at)
            """),
            t,
        )

    # ==== POSTS ====
    posts_data = []
    for _ in range(30):
        posts_data.append(
            {
                "sid": str(uuid.uuid4()),
                "content": fake.text(max_nb_chars=200),
                "thread_sid": random.choice(threads_data)["sid"],
                "user_sid": random.choice(users_data)["sid"],
                "created_at": datetime.now(UTC),
                "updated_at": datetime.now(UTC),
            }
        )

    for p in posts_data:
        session.execute(
            text("""
                INSERT INTO posts.posts (sid, content, thread_sid, user_sid, created_at, updated_at)
                VALUES (:sid, :content, :thread_sid, :user_sid, :created_at, :updated_at)
            """),
            p,
        )

    # ==== POST_VOTES ====
    votes_data = []
    for _ in range(50):
        votes_data.append(
            {
                "sid": str(uuid.uuid4()),
                "post_sid": random.choice(posts_data)["sid"],
                "user_sid": random.choice(users_data)["sid"],
                "value": random.choice([-1, 1]),
                "created_at": datetime.now(UTC),
                "updated_at": datetime.now(UTC),
            }
        )

    for v in votes_data:
        session.execute(
            text("""
                INSERT INTO post_votes.post_votes (sid, post_sid, user_sid, value, created_at, updated_at)
                VALUES (:sid, :post_sid, :user_sid, :value, :created_at, :updated_at)
            """),
            v,
        )

    session.commit()
    session.close()
    print("✅ Database filled with fake data!")


if __name__ == "__main__":
    init_db()
