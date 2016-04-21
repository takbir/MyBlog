# encoding=utf8

from db import dao


def create_blog(**attrs):
    return dao.create_blog(**attrs)


def create_tag(**attrs):
    return dao.create_tag(**attrs)


def add_tags_for_blog(blog, *tags):
    return dao.add_tags_for_blog(blog, *tags)


def get_all_tags():
    return dao.get_all_tags()


def get_blog_pagination(page_num=1, item_per_page=10):
    return dao.get_blog_pagination(page_num, item_per_page)


def update_blog(blog, **attrs):
    dao.update_blog(blog, **attrs)


def update_tag(tag, **attrs):
    dao.update_tag(tag, **attrs)


def get_one_blog(blog_id):
    return dao.get_one_blog(blog_id)


def get_one_tag(tag_id):
    return dao.get_one_tag(tag_id)
