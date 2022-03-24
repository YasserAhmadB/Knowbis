import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateCategories:
    def test_create(self):
        # Arrange

        # Act
        client = APIClient()
        response = client.post('/platform/categories/', {'title': 'a'})

        # Assert

        assert response.status_code == status.HTTP_201_CREATED

    def test_delete(self):
        # Arrange

        # Act
        client = APIClient()
        response = client.delete('/platform/categories/4', {})

        # Assert

        assert response.status_code == status.HTTP_204_NO_CONTENT
