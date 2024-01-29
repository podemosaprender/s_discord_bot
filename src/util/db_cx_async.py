#S: DB Connection, async
from .cfg import cfg_for
from .logging import logm

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError #U: reexport for try:except:

sqlite_file_name = cfg_for("DB_SQLITE_PATH","xdatabase.db") #A: if DB_URL not defined
db_url = cfg_for("DB_URL", f"sqlite+aiosqlite:///{sqlite_file_name}")
logm("DB init connecting to", db_url)
engine= AsyncEngine( create_engine(db_url, echo=False, future=True) )
async_session_maker = sessionmaker(
		engine, class_=AsyncSession, expire_on_commit=False
)

DbWasInit_= False
async def db_init(force=False) -> None:
	global DbWasInit_
	if not DbWasInit_ or force:
		DbWasInit_= True
		async with engine.begin() as conn:
			await conn.run_sync(SQLModel.metadata.create_all)

async def db_session() -> AsyncSession:
	async with async_session_maker() as session:
			yield session

async def save_instance_impl(instance, session):
	session.add(instance)
	await session.commit()
	await session.refresh(instance)

async def save_instance(instance, session= None):
	if session is None:
		async with async_session_maker() as session:
			return await save_instance_impl(instance, session)
	else:
		return await save_instance_impl(instance, session)


