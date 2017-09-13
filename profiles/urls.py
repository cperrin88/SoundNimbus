from django.conf.urls import url

from profiles.apps import ProfilesConfig
from profiles.views import UserProfileView, PostView

app_name = ProfilesConfig.name

urlpatterns = [
    url(r'^$', UserProfileView.as_view()),
    url(r'^post/$', PostView.as_view(), name="post"),
]
