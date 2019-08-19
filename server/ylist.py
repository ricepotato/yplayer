#-*- coding: utf-8 -*-
import os
import sys
import logging

log = logging.getLogger("app.yplayer.server.ylist")

class YList:
    """ 폴더내의 영상 파일과 snapshot, gallery 경로를 찾아
    list 를 생성한다.
    """
    def __init__(self):
        self.mov_ext = ".mp4"
        self.shot_ext = ".jpg"

    def get_list(self, root_path):
        res = []
        for path, dir, files in os.walk(root_path):
            for filename in files:
                if not filename.endswith(self.mov_ext):
                    continue
                
                filepath = os.path.join(path, filename)
                filename_without_ext = filename.replace(self.mov_ext, "")
                snapshot_name = f"{filename_without_ext}_Snapshot{self.shot_ext}"
                snapshot_path = os.path.join(path, snapshot_name)
                shots_path = os.path.join(path, filename_without_ext)

                res.append({
                    "filename":filename, "filepath":filepath,
                    "snapshot":snapshot_path, "shots":self._get_gallery(shots_path)
                })

        return res

    def _get_gallery(self, shots_path):
        shots = []
        if not os.path.exists(shots_path):
            log.warning("shots path not exist. path=%s", shots_path)
            return shots

        for path, dir, files in os.walk(shots_path):
            for filename in files:
                if not filename.endswith(self.shot_ext):
                    continue
                shots.append(os.path.join(path, filename))
        return shots