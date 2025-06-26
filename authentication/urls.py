from django.urls import path
from .views import TokenView, RefreshTokenView

urlpatterns = [
    path('jwt/token/', view=TokenView.as_view(), name='login-view'),
    path('jwt/token/refresh/', view=RefreshTokenView.as_view(), name='refresh-view')
]