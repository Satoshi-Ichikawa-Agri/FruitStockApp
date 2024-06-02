import os
from .base import *


DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
