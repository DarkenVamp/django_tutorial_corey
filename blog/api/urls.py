from django.urls import path
# from blog.api.views import api_post_detail_view
from blog.api.views import APIPostDetailView, APIPostListView

app_name = 'blog'

urlpatterns = [
    path('', APIPostListView.as_view(), name='api-post-list'),
    path('<int:pk>/', APIPostDetailView.as_view(), name='api-post-detail'),
]
