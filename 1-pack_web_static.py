#!/usr/bin/python3
"""
    Module packs a file into an archive
"""


import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """function to archive a file recursively"""
    current = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(current.year,
                                                    current.month,
                                                    current.day,
                                                    current.hour,
                                                    current.minute,
                                                    current.second)
    try:
        local("mkdir -p /versions")
        print("Packing web_static to {}".format(filename))
        local("tar -cvzf /versions/{} ./web_static".format(filename))
        return "/versions/{}".format(filename)
    except Exception:
        return "None"
