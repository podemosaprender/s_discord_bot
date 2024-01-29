#S: Models

from typing import Optional
from pydantic import constr, EmailStr
from sqlmodel import SQLModel, Field, Column, String

from datetime import datetime

TstrNoVacia= constr(strip_whitespace=True, min_length=1) #A: type alias

class Recorte(SQLModel, table=True): #U: Mensaje guardado de Discord Boton
	id: Optional[int] = Field(default=None, primary_key=True) #XXX: campos como en bot
	created_at: datetime = Field( default_factory=datetime.utcnow, ) #XXX: sacaria el default
	saved_by_name: str 
	saved_by_id: str 
	msg_dt: datetime
	msg_id: str
	author_id: str
	author_name: str
	txt: str 




