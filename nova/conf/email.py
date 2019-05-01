from nova.settings import DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

USERS_CREATE_SUPERUSER = DEBUG
USERS_SUPERUSER_EMAIL = 'superuser@djangoproject.com'
USERS_SUPERUSER_PASSWORD = 'django'