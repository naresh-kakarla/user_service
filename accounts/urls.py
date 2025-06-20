from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('', view=RegisterView.as_view())
]