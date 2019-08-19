#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import logging

from flask import jsonify
from flask_restful import Resource, reqparse

log = logging.getLogger("app.yplayer.server.rsrc")

class YListRsrc(Resource):
    """ 주식정보 자원 """
    def __init__(self, **kwargs):
        self.data = kwargs["data"]

    def get(self):
        return jsonify(self.data.get_list())

    def post(self):
        return jsonify(self.data.update_data())