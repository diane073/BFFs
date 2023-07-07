"""
ASGI config for BFFs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from .middleware import JwtAuthMiddlewareStack

import alarm.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFFs.settings")

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": JwtAuthMiddlewareStack(
            URLRouter(alarm.routing.websocket_urlpatterns),
        ),
    }
)
