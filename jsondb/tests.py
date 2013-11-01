#!/usr/bin/env python
import unittest
import os
#import db_handler
from minidb import Minidb as minidb
class MyTests(unittest.TestCase):
        # pylint: disable=R0904

    def setUp(self):
        self.db = minidb("test.db")

    def tearDown(self):
        if os.path.exists("test.db"):
            os.remove("test.db")

    def test_initialization(self):
        self.assertEquals(len(self.db.db), 0)

    def test_get_set(self):
        self.db.set('foo', 'foo')
        foo = self.db.get('foo')
        self.assertEquals(foo,'foo')


if __name__ == "__main__":
    unittest.main()

