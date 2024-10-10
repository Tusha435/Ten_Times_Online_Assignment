from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker  # Updated import
from config import DATABASE_URI
from sqlalchemy.orm import declarative_base  # Updated import

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    published_at = Column(DateTime)  # Add this line for the 'published_at' field
    url = Column(String, unique=True)
    source = Column(String)
    category = Column(String)



# Base = declarative_base()  # No change here after updating the import
#
# class Article(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True)
#     title = Column(String, unique=True)
#     content = Column(Text)
#     published_at = Column(DateTime)
#     url = Column(String, unique=True)
#     source = Column(String)
#     category = Column(String)

# Database connection
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def store_article(article_data):
    if not session.query(Article).filter_by(url=article_data['url']).first():
        article = Article(
            title=article_data['title'],
            content=article_data['content'],
            published_at=article_data['published_at'],
            url=article_data['url'],
            source=article_data['source']
        )
        session.add(article)
        session.commit()

# Initialize the database
def init_db():
    Base.metadata.create_all(engine)
