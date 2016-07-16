# encoding=utf8

"""
Project Exceptions
"""


class ExcConst(object):
    BLOG_NOT_FOUND = 10


EXC_CONST_TRANSLATION = {
    ExcConst.BLOG_NOT_FOUND: u'Blog not found.',
}


def raise_user_exc(exc_code):
    raise ParadasUserException(exc_code)


class ParadasUserException(Exception):

    def __init__(self, exc_code):
        exc_message = EXC_CONST_TRANSLATION.get(
            exc_code,
            u'Exception message not found, please ensure the declaration.')
        message = '<code:{}> {}'.format(exc_code, exc_message)
        super(ParadasUserException, self).__init__(message)
        self.code = exc_code
