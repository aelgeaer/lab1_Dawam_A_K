from app.repositories.sqlalchemy_repo import SQLAlchemyRepository
from app.database import get_db

def get_repository():
    db = next(get_db())
    return SQLAlchemyRepository(db)
