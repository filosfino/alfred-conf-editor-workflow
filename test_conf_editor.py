import os
from os import path

from conf_editor import expand_user_path


def test_expand_user_path():
    assert expand_user_path('~/goodtogo'), path.join(os.getenv('HOME'), 'goodtogo')
