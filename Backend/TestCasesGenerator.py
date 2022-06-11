import re

import inflect

engine = inflect.engine()
import pyperclip


def get_plural(word: str):
    plural = engine.plural(word)
    return plural


model = """class Material(models.Model):  # Course
    PRIVATE_CHOICE = 'Private'
    PUBLIC_CHOICE = 'Public'
    STATUS_CHOICES = [
        ('Pr', PRIVATE_CHOICE),
        ('Pu', PUBLIC_CHOICE),
    ]

    title = models.CharField(max_length=255)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    description = models.CharField(max_length=1255, null=True)
    brief_description = models.CharField(max_length=1255, null=True)

    image = models.ImageField()
    last_update = models.DateField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PRIVATE_CHOICE)
    requirements = models.CharField(max_length=1255, null=True)
    what_will_learn = models.CharField(max_length=1255)

"""
theWord = model.split('(')[0].split(' ')[-1].lower()
attributeRows = re.findall(r"[\w\.-]+ = [\w\.*]+", model)
attributes = ""
jsonObject = [f"{row.split(' ')[0]}: {theWord}.{{row.split(' ')[0]}}," for row in attributeRows]
for i in jsonObject:
    attributes+=i
theWordTitle = theWord.title()
theWordWithS = get_plural(theWord)
theWordWithSTitle = theWordWithS.title()
template = """import pytest
from rest_framework import status
from model_bakery import baker

from _platform.models import """ + theWordTitle + """


@pytest.mark.django_db
class TestGet""" + theWordWithSTitle + """:
    def test_get(self, get_""" + theWord + """):
        # Arrange
        """ + theWord + """ = baker.make(""" + theWordTitle + """)
        # Act
        response = get_""" + theWord + """(""" + theWord + """)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': """ + theWord + """.id,
            'title': """ + theWord + """.title
        }


@pytest.fixture
def get_""" + theWord + """(api_client):
    def do_get_""" + theWord + """(""" + theWord + """):
        return api_client.get(f'/platform/""" + theWordWithS + """/{""" + theWord + """.id}/')

    return do_get_""" + theWord + """


@pytest.mark.django_db
class TestCreate""" + theWordWithSTitle + """:
    def test_create(self, create_""" + theWord + """):
        # Arrange

        # Act
        response = create_""" + theWord + """({'title': 'a'})
        print("response:", response)
        # Assert
        assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def create_""" + theWord + """(api_client):
    def do_create_""" + theWord + """(""" + theWord + """):
        return api_client.post('/platform/""" + theWord + """/', """ + theWord + """)

    return do_create_""" + theWord + """


@pytest.mark.django_db
class TestUpdate""" + theWordWithSTitle + """:
    def test_update(self, update_""" + theWord + """):
        # Arrange
        """ + theWord + """ = baker.make(""" + theWordTitle + """)
        # Act
        response = update_""" + theWord + """(""" + theWord + """, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def update_""" + theWord + """(api_client):
    def do_update_""" + theWord + """(""" + theWord + """, data):
        return api_client.patch(f'/platform/""" + theWordWithS + """/{""" + theWord + """.id}/', data)

    return do_update_""" + theWord + """
entity

@pytest.mark.django_db
class TestDelete""" + theWordWithSTitle + """:
    def test_delete(self, delete_""" + theWord + """):
        # Arrange
        """ + theWord + """ = baker.make(""" + theWordTitle + """)
        # Act
        response = delete_""" + theWord + """(""" + theWord + """, {})

        # Assert
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.fixture
def delete_""" + theWord + """(api_client):
    def do_delete_""" + theWord + """(""" + theWord + """, data):
        return api_client.delete(f'/platform/""" + theWordWithSTitle + """/{""" + theWord + """.id}/', data)

    return do_delete_""" + theWord + """
"""

pyperclip.copy(template)
print(template)
