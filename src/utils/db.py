from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from src.utils.settings import settings

Base=declarative_base()
engine=create_engine(url=settings.Db_Conn)
sessionLocal=sessionmaker(bind=engine)

def get_db():
    session=sessionLocal()
    try:
        yield session
    finally:
        session.close()