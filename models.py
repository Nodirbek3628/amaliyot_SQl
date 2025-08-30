
from datetime import datetime
from sqlalchemy import (
    Column,Table, 
    Integer,String,Text,Boolean,DateTime
)

from database import metadata_obj

tasks = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(length=64)),
    Column('description', Text),
    Column('completed',Boolean,nullable=False,default=False),
    Column('due_date', DateTime,default=datetime.now),
    Column('created_at', DateTime,default=datetime.now),

)

