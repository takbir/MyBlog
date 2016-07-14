# encoding=utf8

from db.models import Blog, Tag, DBSession
from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError


def create_obj(cls=None, **attrs):
    """
    创建对象的基本接口, 会对赋值列表进行检测
    """
    if not cls:
        raise Exception(u'Parameter "cls" cannot be None !')
    obj = cls()
    for k, v in attrs.iteritems():
        if hasattr(obj, k):  # 如果是对象的约定属性才给予赋值
            obj.__setattr__(k, v)
    try:
        DBSession.add(obj)
        DBSession.commit()
    except SQLAlchemyError as exc:
        DBSession.rollback()
        raise exc
    return obj


def create_blog(**attrs):
    """
    创建blog的接口
    """
    blog = create_obj(Blog, **attrs)
    return blog


def add_tags_for_blog(blog, *tags):
    """
    为blog添加Tag m2m关系的接口
    """
    blog.tags.add(*tags)


def create_tag(**attrs):
    """
    创建Tag的接口
    """
    tag = create_obj(Tag, **attrs)
    return tag


def get_all_tags():
    """
    获取所有标签
    """
    return DBSession.query(Tag).order_by('name').all()


def get_blog_pagination(page_num=1, item_per_page=10):
    """
    以分页的方式获取Blog列表
    """
    page_num = int(page_num)
    item_per_page = int(item_per_page)
    return DBSession.query(Blog).order_by(-Blog.updated).slice(
        item_per_page, item_per_page * page_num)


def update_obj(obj, **attrs):
    """
    更新对象接口
    """
    cls = type(obj)
    operation = {}
    for k, v in attrs.iteritems():
        if hasattr(obj, k):
            operation[k] = v
    query = update(cls).where(cls.id == obj.id).values(**operation)
    query.execute()


def update_blog(blog, **attrs):
    """
    更新blog接口
    """
    return update_obj(blog, **attrs)


def update_tag(tag, **attrs):
    """
    更新Tag接口
    """
    return update_obj(tag, **attrs)


def get_one_record(cls, obj_id):
    """
    获取单个记录
    """
    return DBSession.query(cls).get(obj_id)


def get_one_blog(blog_id):
    """
    获取单个Blog
    """
    return get_one_record(Blog, blog_id)


def get_one_tag(tag_id):
    """
    获取单个Tag
    """
    return get_one_record(Tag, tag_id)
