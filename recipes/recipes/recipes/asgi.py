"""
ASGI config for recipes project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

from chat_app import routing

django_asgi_app = get_asgi_application()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipes.settings')

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    )
})

# ASGI_APPLICATION = 'recipes.asgi.application'


####
# from hubble
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hubble_golf.settings")
#
# django_asgi_app = get_asgi_application()
#
# from channels.auth import AuthMiddlewareStack  # noqa: E402
# from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
#
# from chats import routing  # noqa: E402
# from hubble_golf.middleware import JwtAuthMiddleware  # noqa: E402
#
# router_config = {
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#         JwtAuthMiddleware(URLRouter(routing.websocket_urlpatterns))
#     ),
# }
#
# application = ProtocolTypeRouter(router_config)
#
