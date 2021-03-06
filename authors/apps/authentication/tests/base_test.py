"""
    This module contains the base test class
"""

from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt import utils
from django.urls import reverse
from django.test.client import RequestFactory
from rest_framework_jwt.compat import get_user_model

import django
import os

django.setup()

User = get_user_model()


class BaseTestCase(APITestCase):
    """
        Holds the base authentication attributes and test methods
    """

    def setUp(self):
        """
            Creates reusable mock data and test functions.
        """

        self.client = APIClient()
        self.registration_path = reverse('authentication:activation')
        self.new_article_path = reverse('articles:new_article')
        self.articles_feed = reverse('articles:articles_feed')
        self.profile_url = reverse('profiles:list_profiles')
        self.togglenot = reverse('notifications:read-notifications')

        self.view_reports = reverse('articles:view_reports')
        self.username = 'testguy99'
        self.email = 'testguy99'
        self.testuser = User.objects.create_user(self.username, self.email)

        # Article model imported here as it has to wait for django.setup()
        self.payload = utils.jwt_payload_handler(self.testuser)
        self.token = utils.jwt_encode_handler(self.payload)
        self.hauth = 'Bearer {0}'.format(self.token)
        from ...articles.models import Article
        self.article = Article.objects.create(slug='test-slug',
                                              body="some text about something",
                                              tagList=['test'],
                                              author=self.testuser)
        self.article_details = reverse('articles:article_details',
                                       kwargs={'slug': "test-slug"})
        self.report_article = reverse('articles:report_article',
                                      kwargs={'slug': "test-slug"})
        self.report_actions = reverse('articles:report_actions',
                                      kwargs={'pk': 1})
        self.login_path = reverse('authentication:login')
        self.article_rating = reverse('articles:rate_article',
                                      kwargs={'slug': "test-slug"})
        self.social_auth_path = reverse(
            'authentication:social_authentication')
        self.factory = RequestFactory()
        self.forgot_password_url = reverse('authentication:forgot_password')
        self.client.post(
            reverse('highlights:create-highlight',
                    kwargs={"slug": "test-slug"}), {
                        "highlight_object":
                        {"highlight": "text about",
                         "comment": "This quote is innacurate."}
            },
            HTTP_AUTHORIZATION=self.hauth,
            format='json'
        )

        self.user1 = {
            "user": {
                "username": "green",
                "email": "green@gmail.com",
                "password": "greenlantern1#"
            }
        }
        self.user2 = {
            "user": {
                "username": "yellantern",
                "email": "yellantern@gmail.com",
                "password": "yellantern1#"
            }
        }
        self.user3 = {
            "user": {
                "username": "purple",
                "email": "purple@gmail.com",
                "password": "purple1#"
            }
        }
        self.user4 = {
            "user": {
                "username": "blue",
                "email": "blue@gmail.com",
                "password": "purple1#"
            }
        }
        self.first_name = {
            "first_name": "wanyonyi"
        }

        self.user_to_register = {
            'user': {
                'username': 'GoodCow',
                'email': 'cow@mammals.milk',
                'password': 'badA55mammal!'
            }
        }

        self.toggle_on = {
            "email_notification": True
        }

        self.toggle_off = {
            "email_notification": False
        }

        self.google_social_auth = {
            "token_provider": "google-oauth2",
            "access_token": 'access_token'
        }

        self.facebook_social_auth = {
            "token_provider": "facebook",
            "access_token": 'EAAGCNgo8jC4BACqTMo' +
                            '272cv6RQzDgVPzwKAb1ppiL6' +
                            'UTg37ZBCJKVEqg3Vn9YfBGxD' +
                            'sGFg4hc3IydIzxQ2cxzN5kn' +
                            'SQlOeaa6s4iMFL6z3zik1G7' +
                            'SERGJ40ZB2XAOaFKcRttNGc' +
                            'pr4BMKnavMKi9F1VDZC46TW' +
                            'hRZBsTHc30L2nh85VehTHn'
        }

        self.facebook_social_wrong_auth = {
            "token_provider": "facebook",
            "access_token": 'EAAGCNgo8jC4BACqTMo'
        }

        self.twitter_social_auth = {
            "token_provider": "twitter",
            "access_token": 'access_token',
            "access_token_secret": 'access_token_secret'
        }
        self.google_wrong_token = {
            "token_provider": "google-oauth2",
            "access_token": 'wrongtoken!!'
        }

        self.google_invali_provider = {
            "token_provider": "invalidprovider",
            "access_token": os.environ.get('GOOGLE_TOKEN')
        }

        self.user = {
            "user": {
                "email": "authorshaven2@gmail.com",
                "username": "test_me1",
                "password": "testuser!23",
                "bio": "I love programming"
            }
        }

        self.reset_password_data = {
            "password": "Itr!3d21",
            "confirm_password": "Itr!3d21"
        }

        self.reset_password_empty_payload = {
            "email": "",
        }

        self.reset_password_correct_email = {
            "email": "cow@mammals.milk",
        }
        self.mockuser = User.objects.create_user('username', 'username')
        self.title = 'djangorest'

    def register_new_user(self, data={}):
        """
            Creates a new user account and returns the request response
        """
        return self.client.post(self.registration_path,
                                data=data,
                                format='json')

    def forgot_password(self, data):
        return self.client.post(
            self.forgot_password_url,
            data=data,
            format="json")

    def add_credentials(self, response):
        """adds authentication credentials in the request header"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response)

    def report_article(self, report_data):
        self.login_user(self.user)
        self.article
        reverse('report_article', kwargs={'slug': "testslug"})
        response = self.client.post(data=report_data, format='json')
        return response

    def create_superuser(self, email, username, password):
        User.objects.create_superuser(
            email=email,
            username=username, password=password)

    def login_user(self, data):
        return self.client.post(
            self.login_path,
            data,
            format='json'
        ).data

    def login_superuser(self):
        username = self.user['user']['username']
        password = self.user['user']['password']
        email = self.user['user']['email']
        self.create_superuser(email, username, password)
        response = self.login_user(self.user)
        self.add_credentials(response['token'])
