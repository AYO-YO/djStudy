# coding=utf-8
"""

# 异步方式接收网络请求【不要动】

ASGI config for djStudy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djStudy.settings')

application = get_asgi_application()
