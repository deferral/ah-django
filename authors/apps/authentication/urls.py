from django.conf.urls import url
from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
    ForgotPasswordAPIview, ResetPasswordAPIView,
    SocialAuth, VerifyUserAPIView, NotifytoggleAPIView
)
app_name = 'authentication'


urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view(), name="login"),
    url(r'^users/notifications/toggle/(?P<string>[\w\-]+)/?$',
        NotifytoggleAPIView.as_view(), name='notifytoggle'),
    url(r'^account/forgot_password/?$',
        ForgotPasswordAPIview.as_view(), name="forgot_password"),
    url(r'^account/reset_password/?(?P<token>[a-zA-Z0-9_\.-]{3,1000})?/?$',
        ResetPasswordAPIView.as_view(), name="reset_password"),
    url(r'^users/social_auth/?$',
        SocialAuth.as_view(), name='social_authentication'),
    url(r'^users/?$', RegistrationAPIView.as_view(), name='activation'),
    path('users/activate/<auth_payload>/',
         VerifyUserAPIView.as_view(),
         name='account_verification'),
]
