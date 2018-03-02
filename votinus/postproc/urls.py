from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostProcView.as_view(), name='postproc'),
]
