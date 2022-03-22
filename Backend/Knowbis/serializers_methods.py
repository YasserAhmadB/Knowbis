from rest_framework import serializers


def validate_field(string: str):
    """
    :param string:
    :return:
    Used for all fields has to not be empty, all numeric, or starts with a number.
    Rises a serializers.ValidationError if a condition not correct
    """
    if not string:
        raise serializers.ValidationError('Field cannot be empty')

    if string[0].isnumeric():
        raise serializers.ValidationError('Field cannot starts with a number')
