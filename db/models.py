# encoding=utf8

from sqlalchemy import (String,
                        Column,
                        Integer,
                        Text,
                        DateTime,
                        ForeignKey,
                        create_engine)
from sqlalchemy.orm import (sessionmaker,
                            relationship,
                            scoped_session)
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db import make_db_connect_url

BaseORM = declarative_base()

connect_url = make_db_connect_url()

engine = create_engine(connect_url)

BaseORM.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))


class BaseModel(object):
    def to_dict(self):
        """
        将对象结构转化成字典
        """
        return {}


blog_tag_table = Table(
    'blog_tag', BaseORM.metadata,
    Column('blog_id', Integer, ForeignKey('blog.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


class Blog(BaseORM, BaseModel):
    """
    Blog Class
    """
    __tablename__ = u'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now,
                     onupdate=datetime.now)
    tags = relationship('Tag', secondary=blog_tag_table)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S'),
            'updated': self.updated.strftime('%Y-%m-%d %H:%M:%S'),
            'tags': self.tags_to_dict(),
        }

    def tags_to_dict(self):
        """
        获取自身tags的结构列表
        """
        return [t.to_dict() for t in self.tags]


class Tag(BaseORM, BaseModel):
    """
    Tag Class
    """
    __tablename__ = u'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


__db_connected__ = False

if not __db_connected__:
    BaseORM.metadata.create_all()
