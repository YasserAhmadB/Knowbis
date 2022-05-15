import pytest
from rest_framework import status
from model_bakery import baker

from _platform.models import Category


@pytest.mark.django_db
class TestGetCategories:
    def test_get_anonymous_200(self, get_category):
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
    def test_if_anonymous_returns_401(self, create_category):
        # Arrange

        # Act
        response = create_category({'title': 'a'})
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_provider_returns_403(self, create_category, authenticate_provider):
        # Arrange
        authenticate_provider()

        # Act
        response = create_category({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_audience_returns_403(self, create_category, authenticate_audience):
        # Arrange
        authenticate_audience()

        # Act
        response = create_category({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_admin_returns_201(self, create_category, authenticate):
        # Arrange
        authenticate(True)

        # Act
        response = create_category({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def create_category(api_client):
    def do_create_category(category):
        return api_client.post('/platform/categories/', category)

    return do_create_category


@pytest.mark.django_db
class TestUpdateCategories:
    def test_if_anonymous_returns_401(self, update_category):
        # Arrange
        category = baker.make(Category)

        # Act
        response = update_category(category, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_provider_returns_403(self, update_category, authenticate_provider):
        # Arrange
        authenticate_provider()
        category = baker.make(Category)

        # Act
        response = update_category(category, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_audience_returns_403(self, update_category, authenticate_audience):
        # Arrange
        authenticate_audience()
        category = baker.make(Category)

        # Act
        response = update_category(category, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_admin_returns_201(self, update_category, authenticate):
        # Arrange
        authenticate(True)
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


@pytest.mark.django_db
class TestDeleteCategories:
    def test_if_anonymous_returns_401(self, delete_category):
        # Arrange
        category = baker.make(Category)

        # Act
        response = delete_category(category, {})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_provider_returns_403(self, delete_category, authenticate_provider):
        # Arrange
        authenticate_provider()
        category = baker.make(Category)

        # Act
        response = delete_category(category, {})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_audience_returns_403(self, delete_category, authenticate_audience):
        # Arrange
        authenticate_audience()
        category = baker.make(Category)

        # Act
        response = delete_category(category, {})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_admin_returns_201(self, delete_category, authenticate):
        # Arrange
        authenticate(True)
        category = baker.make(Category)

        # Act
        response = delete_category(category, {})

        # Assert
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.fixture
def delete_category(api_client):
    def do_delete_category(category, data):
        return api_client.delete(f'/platform/categories/{category.id}/', data)

    return do_delete_category
