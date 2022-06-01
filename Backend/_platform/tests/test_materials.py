import pytest
from rest_framework import status
from model_bakery import baker

from _platform.models import Material, Provider, Category


@pytest.mark.django_db
class TestGetMaterials:
    def test_get_all_materials(self, get_material, authenticate_provider):
        # Arrange
        material = baker.make(Material)

        # Act
        response = get_material(material)
        data = response.data

        # Assert
        assert response.status_code == status.HTTP_200_OK

        assert data['id'] == material.id
        assert data['title'] == material.title
        assert data['category']['id'] == material.category.id
        assert data['provider']['id'] == material.provider.id
        assert data['duration'] == material.duration
        assert data['description'] == material.description
        assert data['image'] == material.image
        assert data['last_update'] == str(material.last_update)
        assert data['status'] == material.status
        assert data['requirements'] == material.requirements
        assert data['what_will_learn'] == material.what_will_learn

    def test_get_uploaded_materials(self, get_uploaded_material, authenticate_provider):
        # Arrange
        provider = authenticate_provider()
        material = baker.make(Material, provider=provider)

        provider2 = baker.make(Provider)
        material2 = baker.make(Material, provider=provider2)

        # Act
        response = get_uploaded_material()
        data = response.data

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(data) == 1
        data = data[0]

        assert data['id'] == material.id
        assert data['title'] == material.title
        assert data['category']['id'] == material.category.id
        assert data['provider']['id'] == material.provider.id
        assert data['description'] == material.description
        assert data['image'] == material.image
        assert data['last_update'] == str(material.last_update)
        assert data['status'] == material.status
        assert data['requirements'] == material.requirements
        assert data['what_will_learn'] == material.what_will_learn

    def test_get_enrolled_materials(self, get_uploaded_material, authenticate_provider):
        # Arrange
        provider = authenticate_provider()
        material = baker.make(Material, provider=provider)

        provider2 = baker.make(Provider)
        material2 = baker.make(Material, provider=provider2)

        # Act
        response = get_uploaded_material()
        data = response.data

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(data) == 1
        data = data[0]

        assert data['id'] == material.id
        assert data['title'] == material.title
        assert data['category']['id'] == material.category.id
        assert data['provider']['id'] == material.provider.id
        assert data['description'] == material.description
        assert data['image'] == material.image
        assert data['last_update'] == str(material.last_update)
        assert data['status'] == material.status
        assert data['requirements'] == material.requirements
        assert data['what_will_learn'] == material.what_will_learn


@pytest.fixture
def get_material(api_client):
    def do_get_material(material):
        return api_client.get(f'/platform/courses/{material.id}/')

    return do_get_material


@pytest.fixture
def get_uploaded_material(api_client):
    def do_get_material():
        return api_client.get(f'/platform/courses/uploaded/')

    return do_get_material


@pytest.mark.django_db
class TestCreateMaterials:
    def test_if_anonymous_returns_401(self, create_material):
        # Arrange

        # Act
        response = create_material()
        print('response:', response)
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_provider_returns_201(self, create_material, authenticate_provider):
        # Arrange
        authenticate_provider()

        # Act
        response = create_material()

        # Assert
        assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def create_material(api_client):
    def do_create_material(material=None):
        if not material:  # Creates any random material
            material_object = baker.make(Material)
            material = {
                'title': 'material_object.title',
                'category': material_object.category.id,
                'description': 'material_object.description',
                'brief_description': 'material_object.brief_description',
                'image': 'material_object.image',
                'last_update': 'material_object.last_update',
                'status': 'material_object.status',
                'requirements': 'material_object.requirements',
                'what_will_learn': 'material_object.what_will_learn',
                'duration': 'material_object.duration',
            }
            print('material:')
            print(material.values())
        return api_client.post('/platform/courses/', material)

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
