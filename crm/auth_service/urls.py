from django.urls import path

from auth_service.views import (
    UserLoginView,
    UserRegisterView,
    logout_user,
)


app_name = 'auth_service'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]
