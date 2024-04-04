#!/usr/bin/env python3
"""
    Module packs a file into an archive
"""
import os
import datetime
from fabric.api import *

def do_pack():
    """function to archive a file recursively"""
    current = datetime.datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(current.year,
                                      current.month,
                                      current.day,
                                      current.hour,
                                      current.minute,
                                      current.second)
    local("mkdir -p /versions/")
    try:
        print("Packing web_static to {}".format(filename))
        local("tar -cvzf /versions/{} ./web_static".format(filename))
        return ("/versions/{}".format(filename))
    except Exception:
        return "None"
