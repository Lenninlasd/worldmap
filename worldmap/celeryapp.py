from __future__ import absolute_import

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worldmap.settings')

app = Celery('worldmap')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
