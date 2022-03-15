from rest_framework import serializers


def validate_field(title: str):
    if not title:
        raise serializers.ValidationError('Field cannot be empty')

    if title[0].isnumeric():
        raise serializers.ValidationError('Field cannot starts with a number')
