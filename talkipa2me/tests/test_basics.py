from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from pytest import mark


@mark.django_db()
def test_admin_response(client):
    response = client.get('/admin/login/')
    assert response.status_code == 200


@mark.django_db()
def test_database():
    get_user_model().objects.all().exists()
