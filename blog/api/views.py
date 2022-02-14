from blog.models import Post
from rest_framework.generics import RetrieveAPIView, ListAPIView
from blog.api.serializers import PostSerializer


class APIPostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class APIPostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
