# app/repositories/admin_logs/admin_logs.py
from app.models import AdminLogs
from app.repositories.BaseRepository import BaseRepository
from app.schemas import AdminLogCreate, AdminLogUpdate


class AdminLogRepository(BaseRepository[AdminLogs, AdminLogCreate, AdminLogUpdate]):
    pass


admin_log_repository = AdminLogRepository(AdminLogs)
