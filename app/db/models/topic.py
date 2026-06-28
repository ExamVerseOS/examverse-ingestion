from sqlalchemy import Column, String
from app.db.base import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(String, primary_key=True)
    name = Column(String)
    parent_exam = Column(String)
    type = Column(String)