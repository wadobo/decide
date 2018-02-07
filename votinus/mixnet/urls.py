from django.urls import path

from . import views


urlpatterns = [
    path('gen-key/<int:id_votation>/', views.GenerateKey.as_view(), name='generate_key'),
]
