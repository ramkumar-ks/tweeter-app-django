from .views import CommentViewSet
from rest_framework.urls import path

comments_view = CommentViewSet.as_view()

urlpatterns = [
    path('comments/<int:id>', comments_view, name='comments'),
]
