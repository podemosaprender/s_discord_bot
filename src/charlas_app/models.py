#S: Models

from typing import Optional
from pydantic import constr, EmailStr
from sqlmodel import SQLModel, UniqueConstraint, Field, Column, String, DateTime

from datetime import datetime

TstrNoVacia= constr(strip_whitespace=True, min_length=1) #A: type alias

class Recorte(SQLModel, table=True): #U: Mensaje guardado de Discord Boton
	__table_args__ = ( 
		UniqueConstraint("msg_id", "msg_dt", name="recorte_uniq_id_and_dt"),
	)
	id: Optional[int] = Field(default=None, primary_key=True) 
	created_at: datetime = Field( default_factory=datetime.utcnow, sa_column=Column(DateTime(timezone=True), nullable=False)) #A: timezone necesario sino da error en postgresql
	saved_by_name: str 
	saved_by_id: str 
	msg_dt: datetime
	msg_id: str
	author_id: str
	author_name: str
	channel_id: str
	channel_name: str
	tags: str
	txt: str 




