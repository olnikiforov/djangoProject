from django.apps import apps
from django.test import TestCase
from django.urls import reverse
from main.apps import MainConfig
from main.models import Author



class MainConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(MainConfig.name, 'main')
        self.assertEqual(apps.get_app_config('main').name, 'main')


def test_homepage(client):
    response = client.get(reverse('homepage'))
    assert response.status_code == 200


def test_about(client):
    response = client.get(reverse('about'))
    assert response.status_code == 200


def test_posts(client):
    response = client.get(reverse('posts'))
    assert response.status_code == 200


def test_posts_list(client):
    response = client.get(reverse('posts_list'))
    assert response.status_code == 200


def test_post_create(client):
    response = client.get(reverse('post_create'))
    assert response.status_code == 200


def test_xlsx(client):
    response = client.get(reverse('posts_xlsx'))
    assert response.status_code == 200


def test_api_author(client):
    response = client.get(reverse('api_authors_new'))
    assert response.status_code == 200


def test_api_subscribe(client):
    response = client.get(reverse('api_subscribe'))
    assert response.status_code == 200


def test_subscribers_notify(client):
    response = client.get(reverse('subscribers_notify'))
    assert response.status_code == 200


def test_api_post(client):
    response = client.get(reverse('api_post'))
    assert response.status_code == 200


def test_api_categories(client):
    response = client.get(reverse('categories'))
    assert response.status_code == 200


def test_author_delete(client):
    response = client.get(reverse('delete_author'))
    assert response.status_code == 200


def test_post_delete(client):
    response = client.get(reverse('delete_posts'))
    assert response.status_code == 200


def test_contact_us_post_form(client):
    response = client.post(reverse('contact-us-create'))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Обязательное поле.'],
        'topic': ['Обязательное поле.'],
        'text': ['Обязательное поле.']
    }


def test_contact_us_correct_form(client):
    response = client.post(reverse('contact-us-create'), data={
        'email_to': 'testing@gmail.com',
        'topic': 'smth',
        'text': 'message01',
    })
    assert response.status_code == 200


def test_contact_us_post_wrong_email(client):
    response = client.post(reverse('contact-us-create'), data={
        'email_to': 'not-valid-email_to'
    })
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Введите правильный адрес электронной почты.'],
        'topic': ['Обязательное поле.'],
        'text': ['Обязательное поле.']
    }


def test_authors_new(client):
    start = Author.objects.count()
    response = client.get(reverse("authors_new"))
    assert response.status_code == 200
    assert Author.objects.count() == start + 1
