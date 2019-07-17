from django.conf.urls import url
from .views import ListCreateFollow, DeleteFollower
from .views import FollowersView, RetrieveFollowing

app_name = 'followers'

urlpatterns = [
    url(r'^profiles/?/(?P<user_id>[\d]+)?/?/follow/?$',
        ListCreateFollow.as_view(), name='follow_url'),
    url(r'^profiles/?/(?P<user_id>[\d]+)?/?/unfollow',
        DeleteFollower.as_view(), name='delete_url'),
    url(r'^profiles/?/(?P<user_id>[\d]+)?/?/followers/',
        FollowersView.as_view(), name='followers_url'),
    url(r'^profiles/?/(?P<user_id>[\d]+)?/?/following/',
        RetrieveFollowing.as_view(), name='following_url'),
]
