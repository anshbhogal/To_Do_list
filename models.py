from sqlalchemy import Column, Integer, String,ForeignKey, Boolean, Text, Date, create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    details = Column(Text, nullable=True)
    deadline = Column(Date, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    def __str__(self):
        return f"Task id = {self.id},Task name = '{self.title}' and Deadline = {self.deadline}"

# Set default database URL if not provided
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///taskmaster.db")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)