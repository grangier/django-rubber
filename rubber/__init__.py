"""
Init for rubber.
"""
import django

from .version import __version__  # noqa

from rubber.apps import get_rubber_config  # noqa

# default_app_config is deprecated in Django 3.2+ (auto-discovery)
# but required for Django 3.0/3.1
if django.VERSION < (3, 2):
    default_app_config = 'rubber.apps.RubberConfig'
