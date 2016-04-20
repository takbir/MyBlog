# encoding=utf8

from packages import peewee as pw
from packages.playhouse import fields
from datetime import datetime
import settings

# db = pw.SqliteDatabase('db/blog.db3')
db = pw.MySQLDatabase(settings.MYSQL_DBNAME,
                      user=settings.MYSQL_USER,
                      host=settings.MYSQL_HOST,
                      password=settings.MYSQL_PASSWD,
                      port=settings.MYSQL_PORT)


class BaseModel(pw.Model):
    class Meta:
        database = db

    def to_dict(self):
        """
        将对象结构转化成字典
        """
        return {}


class Blog(BaseModel):
    """
    Blog Class
    """
    id = pw.PrimaryKeyField()
    title = pw.CharField(max_length=255)
    content = pw.TextField()
    created = pw.DateTimeField(default=datetime.now)
    updated = pw.DateTimeField(default=datetime.now)

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


class Tag(BaseModel):
    """
    Tag Class
    """
    id = pw.PrimaryKeyField()
    name = pw.CharField(max_length=100)
    blogs = fields.ManyToManyField(Blog, related_name='tags')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


BlogTagThrough = Tag.blogs.get_through_model()


__db_connected = False

if not __db_connected:
    db.connect()
    db.create_tables([Blog, Tag, BlogTagThrough], safe=True)
