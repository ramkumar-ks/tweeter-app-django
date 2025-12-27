from django.urls import path
from .views import FollowerView

follower_url = FollowerView.as_view()

urlpatterns = [
    path('followers/', follower_url, name='follow'),
]