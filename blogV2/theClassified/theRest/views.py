from http.client import HTTPResponse
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# Create your views here.


class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, 
                mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
       




# ViewSets

# class PostViewSet(viewsets.ViewSet):
#     def list(self, request):
#         posts = Post.objects.all()
#         serializer  = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer  = PostSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_object(self, slug):
#         try:
#             posts = Post.objects.get(slug=slug)
#         except Post.DoesNotExist:
#             raise Http404

#     def retrieve(self, request, slug):
#         post = self.get_object(slug)
#         serializer  = PostSerializer(post)
#         return Response(serializer.data)

#     def update(self, request, slug):
#         post = self.get_object(slug)
#         serializer  = PostSerializer(post, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, slug):
#         post = self.get_object(slug)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Generic API View

# class PostList(generics.ListCreateAPIView, generics.ListAPIView, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class  = PostSerializer



# class PostDetail(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class  = PostSerializer
#     lookup_fields = ['slug']



# Mixins
# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class  = PostSerializer


#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)




# class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class  = PostSerializer
#     lookup_fields = ['slug']


#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update(request, slug=slug)

#     def delete(self, request, slug):
#         return self.destroy(request, slug=slug)


# Class based views

# class PostList(APIView):

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDetail(APIView):

#     def get_object(self, slug):
#         try:
#             posts = Post.objects.get(slug=slug)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, slug):
#         post = self.get_object(slug)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         post = self.get_object(slug)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         post = self.get_object(slug)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# View Decorators
# @api_view(['POST', 'GET'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT', 'GET', 'DELETE'])
# def post_detail(request, slug):

#     try:
#         post = Post.objects.get(slug=slug)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer=PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# no decorator
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)


#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error, status=400)



# def post_detail(request, slug):

#     try:
#         post = Post.objects.get(slug=slug)
#     except Post.DoesNotExist:
#         return HTTPResponse(status=404)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer=PostSerializer(post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         post.delete()
#         return HTTPResponse(status=204)