import datetime

from django.test import TestCase

# Create your tests here.
print(datetime.datetime.now().date() + datetime.timedelta(weeks=6))
