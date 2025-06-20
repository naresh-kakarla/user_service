from django.urls import path
from .views import RegisterAppClientView, DeleteAPPClientView


urlpatterns = [
    path('register/', RegisterAppClientView.as_view()),
    path('<str:client_name>/', DeleteAPPClientView.as_view())
]