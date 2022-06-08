from datetime import timedelta

AUTH_USER_MODEL = 'users_manager.User'  # For authenticator
REST_FRAMEWORK = {  # For authenticator
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',  # OAuth2, JWT
    # ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Up to you to decide, depends on your project
    )
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30)  # the login token lifetime, default was 5m
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'users_manager.User.serializer.UserCreateSerializer',
        'user': 'users_manager.User.serializer.UserRetrieveSerializer',
        'current_user': 'users_manager.User.serializer.UserRetrieveSerializer',
    }
}

PASSWORD_RESET_CONFIRM_URL = 'http://127.0.0.1:8000/auth/users/reset_password_confirm/'
