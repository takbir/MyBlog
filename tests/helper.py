# encoding=utf8

import random
import string
import datetime
from db.models import Blog


letters = string.ascii_letters + string.digits


def random_str(length=10):
    strs = [random.choice(letters) for i in xrange(length)]
    return ''.join(strs)


def gen_fake_blog():
    blog = Blog()
    blog.id = random.randint(100000, 100999)
    blog.title = random_str()
    blog.content = random_str(100)
    blog.created = datetime.datetime.now()
    blog.updated = datetime.datetime.now()
    blog.tags = []
    return blog
