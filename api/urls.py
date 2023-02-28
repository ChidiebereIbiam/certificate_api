from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('certificate/', views.Certificate_List.as_view(), name="certificate"),
    path('certificate/<int:id>/', views.certificate_detail),
    path('verify/<int:id>/', views.VerifyCertificate.as_view()),
]
