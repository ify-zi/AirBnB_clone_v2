#!/usr/bin/python3
"""
    Module deploys compress file to servers
"""


import os
from fabric.api import env, run, put


env.hosts = ['52.87.219.34', '100.25.132.43']
env.key_filename = "~/.ssh/school"
env.user = 'ubuntu'

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
        return True
    except Exception:
        return False
