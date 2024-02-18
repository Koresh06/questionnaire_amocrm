from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

import config

engine = create_async_engine(
    url=config.SQLALCHEMY_URL,
    echo=config.SQLALCHEMY_ECHO
)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    username_tg: Mapped[str] = mapped_column(String())
    
    name: Mapped[str] = mapped_column(String())
    phone: Mapped[str] = mapped_column(String())
    inst: Mapped[str] = mapped_column(String())
    descriphion: Mapped[str] = mapped_column(String())
    result: Mapped[bool] = mapped_column(default=False)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)