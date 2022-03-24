import pytest
from rest_framework import status
from model_bakery import baker

from _platform.models import Category


@pytest.mark.django_db
class TestGetCategories:
    def test_get(self, get_category):
        # Arrange
        category = baker.make(Category)
        # Act
        response = get_category(category)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': category.id,
            'title': category.title
        }


@pytest.fixture
def get_category(api_client):
    def do_get_category(category):
        return api_client.get(f'/platform/categories/{category.id}/')

    return do_get_category


@pytest.mark.django_db
class TestCreateCategories:
    def test_create(self, create_category):
        # Arrange

        # Act
        response = create_category({'title': 'a'})
        print("response:", response)
        # Assert
        assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def create_category(api_client):
    def do_create_category(category):
        return api_client.post('/platform/categories/', category)

    return do_create_category


@pytest.mark.django_db
class TestUpdateCategories:
    def test_update(self, update_category):
        # Arrange
        category = baker.make(Category)
        # Act
        response = update_category(category, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def update_category(api_client):
    def do_update_category(category, data):
        return api_client.patch(f'/platform/categories/{category.id}/', data)

    return do_update_category
