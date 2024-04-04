#!/usr/bin/python3
"""
    Module deploys compress file to servers
"""


import os
from fabric.api import *


env.hosts = ['52.87.219.34', '100.25.132.43']


def do_deploy(archive_path):
    """
        deploy code to sever
    """

    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    foldername = filename.replace(".tgz", "")
    folderpath = "/data/web_static/releases/{}/".format(foldername)
    try:
        put(archive_path, "/tmp/{}".format(filename))
        run("sudo mkdir -p {}".format(folderpath))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, folderpath))
        run("sudo rm -rf /tmp/{}".format(filename))
        run("sudo mv {}web_static/* {}".format(folderpath, folderpath))
        run("sudo rm -rf {}web_static".format(folderpath))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folderpath))
        print("Deployed")
        return True
    except Exception:
        return False
