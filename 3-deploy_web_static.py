#!/usr/bin/python3
"""
    Module does a full deployement
    from packing to archive, then extraction
    and deployment
"""


import os
from datetime import datetime
from fabric.api import env, run, put, runs_once, local


env.hosts = ['52.87.219.34', '100.25.132.43']
env.key_filename = "~/.ssh/school"
env.user = 'ubuntu'


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
        return ("{}".format(filename))
    except Exception:
        return "None"


def do_deploy(archive_path):
    """
        deploy code to sever
    """

    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1].split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run('mkdir -p /data/web_static/releases/{}/'.format(file_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(file_name, file_name))
        run('rm /tmp/{}.tgz'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(file_name))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """ function calls other fucntions"""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
