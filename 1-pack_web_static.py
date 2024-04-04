#!/usr/bin/python3
"""
    Module packs a file into an archive
"""


import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """function to archive a file recursively"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    current = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(current.year,
                                                             current.month,
                                                             current.day,
                                                             current.hour,
                                                             current.minute,
                                                             current.second)
    try:
        print("Packing web_static to {}".format(filename))
        local("tar -cvzf {} web_static".format(filename))
        file_size = os.stat(filename).st_size
        print("web_static packed: {} -> {} Bytes".format(filename, file_size))
    except Exception:
        return "None"
