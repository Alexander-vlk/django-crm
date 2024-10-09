from django.urls import path

from auth_service.views import (
    UserLoginView,
    # register,
    logout_user
)


app_name = 'auth_service'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
