from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    mensaje = Column(String)

    intent = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)