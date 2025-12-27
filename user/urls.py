from django.urls import path
from .views import UserProfileView, UserView

user_profile = UserProfileView.as_view()
user = UserView.as_view()

urlpatterns = [
    path('register/', user, name='user'),
    path('profile/', user_profile, name='user_profile'),
]
