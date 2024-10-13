from django.urls import path


from dashboard.views import (
    dashboard_index
)


app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_index, name='dashboard_index'),
]
