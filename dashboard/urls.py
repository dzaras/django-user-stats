
from django.urls import path
from .views import user_stats, user_stats_page

urlpatterns = [
    path('', user_stats_page, name='stats_page'),  # this is the frontend
    path('stats/', user_stats, name='user_stats'), # this is the JSON API
]
