#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    archive_path = 'versions/web_static_{}.tgz'\
        .format(datetime.now().strftime('%Y%m%d%H%M%S'))

    if not os.path.exists('versions'):
        os.makedirs('versions')

    result = local('tar -cvzf {} web_static'.format(archive_path))

    if result.return_code != 0:
        return None
    else:
        return archive_path
