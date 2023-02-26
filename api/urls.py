from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('certificate/', views.Certificate_List.as_view(), name="certificate"),
]
