#-*- coding: utf-8 -*-
import os
import sys
import json
import logging

cur_path = os.path.dirname(__file__)
ds_path = os.path.join(cur_path, "ds")

log = logging.getLogger("app.yplayer.server.data")

class DataControl:
    def __init__(self, ylist):
        self.ylist = ylist
        self.ds_src_path = os.path.join(ds_path, "datasource.json")
        self.cfg = self._get_conf()
        self.root_path = cfg["root_path"]

    def update_data(self):
        ylist_obj = ylist.get_list(self.root_path)
        with open(self.ds_src_path, "w") as f:
            f.write(json.dumps(ylist_obj))
        return True

    def get_list(self):
        ylist_obj = []
        if os.path.exists(self.ds_src_path):
            ylist_obj = self._get_list_from_file()

        return ylist_obj

    def _get_list_from_file(self):
        with open(self.ds_src_path, "r") as f:
            data = f.read()
        ylist_obj = json.loads(data)
        return ylist_obj



    def _get_conf(self):
        conf_path = os.path.join(cur_path, "data.conf")
        with open(conf_path, "r") as f:
            data = f.read()
        return json.loads(data)



