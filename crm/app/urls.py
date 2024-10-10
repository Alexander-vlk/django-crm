from django.urls import path


from app.views import IndexPageView


app_name = 'app'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
