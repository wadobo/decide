from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.MixnetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shuffle/<int:voting_id>/', views.Shuffle.as_view(), name='shuffle'),
    path('decrypt/<int:voting_id>/', views.Decrypt.as_view(), name='decrypt'),
]
