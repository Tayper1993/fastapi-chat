from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


database_url = 'sqlite+aiosqlite:///db.sqlite3'
engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
