from django.urls import path
from django.views.decorators.cache import cache_page


from app.views import IndexPageView


app_name = 'app'
urlpatterns = [
    path('', cache_page(60 * 15)(IndexPageView.as_view()), name='index'),
]
