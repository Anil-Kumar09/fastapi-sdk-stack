"""SQLAlchemy models"""
from sqlalchemy import Column,ForeignKey,Integer,String,Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer,primary_key= True,index = True)
    gsis_id = Column(String,nullable = True)
