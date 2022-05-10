from datetime import timedelta

AUTH_USER_MODEL = 'authenticator.User'  # For authenticator
REST_FRAMEWORK = {  # For authenticator
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',  # OAuth2, JWT
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.AllowAny', # Up to you to decide, depends on your project
    # )
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30)  # the login token lifetime, default was 5m
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'authenticator.serializers.UserCreateSerializer',
        'user': 'authenticator.serializers.UserRetrieveSerializer',
        'current_user': 'authenticator.serializers.UserRetrieveSerializer',
    }
}
