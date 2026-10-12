from sqlalchemy import create_engine, Column, INTEGER, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///Social_Media.db')
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'usersInfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    username = Column(String)

    posts = relationship('Post', back_populates='owner' )

class Post(Base):
    __tablename__ = 'postsInfo'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)

    user_id = Column(INTEGER, ForeignKey('usersInfo.id'))

    owner = relationship('User', back_populates='posts')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
sessionLocal = Session()