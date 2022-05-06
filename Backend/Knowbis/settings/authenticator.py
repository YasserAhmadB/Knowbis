from datetime import timedelta

AUTH_USER_MODEL = 'authenticator.User'  # For authenticator
REST_FRAMEWORK = {  # For authenticator
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30)  # the login token lifetime, default was 5m
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'authenticator.serializers.UserCreateSerializer',
        'user': 'authenticator.serializers.UserRetrieveSerializer',
        'current_user': 'authenticator.serializers.UserRetrieveSerializer',
    }
}
