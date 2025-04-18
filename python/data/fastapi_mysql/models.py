from sqlalchemy import Column, Text, INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class St_info(Base):
    __tablename__ = 'st_info'

    ST_ID = Column(INT, primary_key=True,nullable=False)
    NAME = Column(Text,nullable=False)
    DEPT = Column(Text,nullable=False)

class St_grade(Base):
    __tablename__ = 'st_grade'

    ST_ID = Column(INT, primary_key=True,nullable=False)
    Linux = Column(Text,nullable=False)
    DB = Column(Text,nullable=False)

