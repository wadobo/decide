from django.urls import path
from . import views


urlpatterns = [
    path('<str:submodule><path:route>', views.Gateway.as_view(), name='gateway'),
]
