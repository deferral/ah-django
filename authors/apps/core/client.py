import os
from django.contrib.sites.shortcuts import get_current_site


def get_domain():
    return os.getenv('CLIENT_DOMAIN', '')


def get_password_reset_link(request, token):
    '''
    :param:client_url for front-end application
    '''
    """
    client_url refers to the front-end application reset url
    e.g http://ah-django/deferral/reset-password
    """

    front_end_domain = os.getenv('FRONTEND_DOMAIN')
    return 'http://{}/{}'.format(front_end_domain, token)
