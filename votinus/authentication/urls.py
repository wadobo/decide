from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import GetUserView


urlpatterns = [
    path('login/', obtain_auth_token),
    path('getuser/', GetUserView.as_view()),
]
