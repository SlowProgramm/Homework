"""
создайте алхимичный engine +
добавьте declarative base (свяжите с engine) +
создайте объект Session +
добавьте модели User и Post, объявите поля: +
для модели User обязательными являются name, username, email +
для модели Post обязательными являются user_id, title, body +
создайте связи relationship между моделями: User.posts и Post.user +
"""

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship
)
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
import os

DB_ECHO = True
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:Doctor8897@localhost:5432/postgres"
engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=DB_ECHO)
Base = declarative_base(bind=engine)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "hw4_users"
    json_id = Column(Integer)
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    username = Column(String(100), unique=False, nullable=False)
    email = Column(String, unique=False, nullable=False)
    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"


class Post(Base):
    __tablename__ = "hw4_posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("hw4_users.id"), nullable=False, unique=False)
    title = Column(String(100), unique=False, nullable=False, default="")
    body = Column(String(999), unique=False, nullable=False, default="")
    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return f"Post(id={self.id}, user_id={self.user_id!r}, title={self.title!r})"


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
