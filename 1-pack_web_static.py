#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack():
    archive_folder = 'web_static'
    archive_name = 'web_static_{}.tgz'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
    archive_path = 'versions/{}'.format(archive_name)

    if not os.path.exists('versions'):
        os.makedirs('versions')

    result = os.system('tar -cvzf {} {}'.format(archive_path, archive_folder))

    if result != 0:
        return None
    else:
        return archive_path
