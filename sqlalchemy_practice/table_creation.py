"""
Desc: table creation in sqlalchemy

"""

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

meta = MetaData()

engine = create_engine("sqlite:///college.db", echo=True)

students = Table(
    "students", meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
)
meta.create_all(engine)
