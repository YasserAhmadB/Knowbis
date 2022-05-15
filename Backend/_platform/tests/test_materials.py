import pytest
from rest_framework import status
from model_bakery import baker

from _platform.models import Material


@pytest.mark.django_db
@pytest.mark.skip
class TestGetMaterials:
    def test_get(self, get_material):
        # Arrange
        material = baker.make(Material)
        # Act
        response = get_material(material)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': material.id,
            'title': material.title,
            'category': material.category,
            'provider': material.provider,
            'description': material.description,
            'brief_description': material.brief_description,
            'image': material.image,
            'last_update': material.last_update,
            'status': material.status,
            'requirements': material.requirements,
            'what_will_learn': material.what_will_learn
        }


@pytest.fixture
def get_material(api_client):
    def do_get_material(material):
        return api_client.get(f'/platform/materials/{material.id}/')

    return do_get_material


@pytest.mark.django_db
@pytest.mark.skip
class TestCreateMaterials:
    def test_create(self, create_material):
        # Arrange

        # Act
        response = create_material({'title': 'a'})
        print("response:", response)
        # Assert
        assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def create_material(api_client):
    def do_create_material(material):
        return api_client.post('/platform/material/', material)

    return do_create_material


@pytest.mark.django_db
@pytest.mark.skip
class TestUpdateMaterials:
    def test_update(self, update_material):
        # Arrange
        material = baker.make(Material)
        # Act
        response = update_material(material, {'title': 'New title'})

        # Assert
        assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def update_material(api_client):
    def do_update_material(material, data):
        return api_client.patch(f'/platform/materials/{material.id}/', data)

    return do_update_material


@pytest.mark.django_db
@pytest.mark.skip
class TestDeleteMaterials:
    def test_delete(self, delete_material):
        # Arrange
        material = baker.make(Material)
        # Act
        response = delete_material(material, {})

        # Assert
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.fixture
def delete_material(api_client):
    def do_delete_material(material, data):
        return api_client.delete(f'/platform/Materials/{material.id}/', data)

    return do_delete_material
