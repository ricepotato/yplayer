#-*- coding: utf-8 -*-
import os
import sys
import unittest
import logging

log = logging.getLogger("app.yplayer.test.ylist")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)

cur_path = os.path.dirname(__file__)
base_path = os.path.abspath(os.path.join(cur_path, "..", "server"))
sys.path.append(base_path)

from ylist import YList

class TestYList(unittest.TestCase):
    def setUp(self):
        self.ylist = YList("C:\\Users\\sukju\\Downloads")

    def tearDown(self):
        pass

    def test_list(self):
        items = self.ylist.get_list()
        self.assertIsNotNone(items)
        self.assertEqual(len(items), 3)
        for item in items:
            self.assertTrue(os.path.exists(item["filepath"]))
            self.assertTrue(os.path.exists(item["snapshot"]))

if __name__ == "__main__":
    unittest.main()
    