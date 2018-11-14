from __future__ import absolute_import
from ._version import __version__
from .app import IRFlowService


def get_version():
    """
    Returns the version of the package

    :return: The version of the package
    """
    return __version__
