from django.urls import path
from .views import PostListView, PostDetailView, test_404

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path("<str:pk>/", PostDetailView.as_view(), name='detailView'),
    path('test-404/', test_404),
]