"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# BASE_DIR ni o'zingiz aniqlashingiz kerak:
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
