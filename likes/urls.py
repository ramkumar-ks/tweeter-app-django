from .views import LikeViewSet
from django.urls import path

likes_view = LikeViewSet.as_view()

urlpatterns = [
    path('likes/<int:id>', likes_view, name="likes"),
]