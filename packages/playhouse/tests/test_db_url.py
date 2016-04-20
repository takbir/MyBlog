from peewee import *
from playhouse.db_url import connect, parse
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.tests.base import PeeweeTestCase


class TestDBURL(PeeweeTestCase):
    def test_db_url_parse(self):
        cfg = parse('mysql://usr:pwd@hst:123/db')
        self.assertEqual(cfg['user'], 'usr')
        self.assertEqual(cfg['passwd'], 'pwd')
        self.assertEqual(cfg['host'], 'hst')
        self.assertEqual(cfg['database'], 'db')
        self.assertEqual(cfg['port'], 123)
        cfg = parse('postgresql://usr:pwd@hst/db')
        self.assertEqual(cfg['password'], 'pwd')
        cfg = parse('mysql+pool://usr:pwd@hst:123/db'
                    '?max_connections=42&stale_timeout=8001')
        self.assertEqual(cfg['user'], 'usr')
        self.assertEqual(cfg['password'], 'pwd')
        self.assertEqual(cfg['host'], 'hst')
        self.assertEqual(cfg['database'], 'db')
        self.assertEqual(cfg['port'], 123)
        self.assertEqual(cfg['max_connections'], '42')
        self.assertEqual(cfg['stale_timeout'], '8001')

    def test_db_url(self):
        db = connect('sqlite:///:memory:')
        self.assertTrue(isinstance(db, SqliteDatabase))
        self.assertEqual(db.database, ':memory:')

        db = connect('sqlite:///:memory:', journal_mode='MEMORY')
        self.assertTrue(('journal_mode', 'MEMORY') in db._pragmas)

        db = connect('sqliteext:///foo/bar.db')
        self.assertTrue(isinstance(db, SqliteExtDatabase))
        self.assertEqual(db.database, 'foo/bar.db')

        db = connect('sqlite:////this/is/absolute.path')
        self.assertEqual(db.database, '/this/is/absolute.path')

        db = connect('sqlite://')
        self.assertTrue(isinstance(db, SqliteDatabase))
        self.assertEqual(db.database, ':memory:')

    def test_bad_scheme(self):
        def _test_scheme():
            connect('missing:///')

        self.assertRaises(RuntimeError, _test_scheme)