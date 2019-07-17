from django.urls import reverse
from rest_framework_jwt.compat import get_user_model
from rest_framework.test import APITestCase, APIClient

User = get_user_model()
class FollowerBaseTest(APITestCase):
    """
    A base test containing for followers tests file
    """

    def setUp(self):
        """Auth to be run for every test"""
        self.user = {
            "user": {
                "username": "cowmammal",
                "email": "cowmammal@milk.com",
                "password": "testUse1@#"
            }
        }

        self.user1 = {
            "user": {
                "username": "testuser",
                "email": "test@this.com",
                "password": "testT23#!"
            }
        }

        self.followed_user = {
            "username": "testuser"
        }

        self.follow_user = {
            "username": "cowmammal"
        }

        self.non_existent_user = {
            "username": "goatmammal"
        }

        self.follow_self = {
            "username": "cowmammal"
        }

        self.client = APIClient()
        self.registration_path = reverse('authentication:activation')
        self.login_path = reverse('authentication:login')
        # self.follow_url = reverse('followers:follow_url', kwargs={
        #     "user_id": self.user_id})

        # self.follow_self_url = reverse('followers:follow_url', kwargs={
        #     "user_id": self.user_id})

        # self.unfollow_url = reverse('followers:delete_url', kwargs={
        #     "user_id": self.user_id
        # })
        # self.following_list_url = reverse('followers:following_url', kwargs={
        #     "user_id": self.user_id
        # })
        # self.followers_url = reverse('followers:followers_url', kwargs={
        #     "user_id": self.user_id
        # })

    def register_user(self, data):
        return self.client.post(
            self.registration_path,
            data,
            format='json'
        )

    def login_a_user(self, data):
        return self.client.post(
            self.login_path,
            data,
            format='json'
        ).data

    def authorize_user(self, user_login_details):
        """
        Generated token for protected endpoints
        """
        with self.settings(
                EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
            self.register_user(data=self.user)
        payload = self.login_a_user(data=user_login_details)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + payload['token'])
