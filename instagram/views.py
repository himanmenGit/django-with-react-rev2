from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PublicPostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body : ", request.body)
        print("request.body : ", request.POST)
        return super().dispatch(request, *args, **kwargs)
