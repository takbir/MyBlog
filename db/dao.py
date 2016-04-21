# encoding=utf8

from db.models import Blog, Tag


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
    obj.save()
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
    return Tag.select().order_by(Tag.name)


def get_blog_pagination(page_num=1, item_per_page=10):
    """
    以分页的方式获取Blog列表
    """
    page_num = int(page_num)
    item_per_page = int(item_per_page)
    return Blog.select().order_by(-Blog.updated).paginate(page_num, item_per_page)
