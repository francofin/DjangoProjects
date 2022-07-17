from django.shortcuts import render, HttpResponse
from yaml import serialize
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
# Create your views here.


# Listing and Posting articles


# Generic View Sets
class ArticleViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer
    lookup_field = 'slug'


    permission_classes = [IsAuthor]
    # authentication_classes = (TokenAuthentication, SessionAuthentication)


# ModelViewSet
'''
class ArticleViewSet(viewsets.ModelViewSet):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer
    lookup_field = 'slug'


'''
'''
# Mixins

class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, slug, *args, **kwargs):
        return self.retrieve(request, slug=slug)

    def put(self, request, slug, *args, **kwargs):
        return self.update(request, slug=slug)

    def delete(self, request, slug, *args, **kwargs):
        return self.destroy(request, slug=slug)
'''

'''
# ViewSets
class ArticleViewSet(viewsets.ViewSet):


    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


'''



'''
# Generic Class Based View, look is the same as above.
class ArticleList(generics.ListCreateAPIView):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Article.objects.all()
    serializer_class  = ArticleSerializer
    lookup_field = 'slug'

'''

'''
# Class based View
class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, stauts = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = self.get_object(slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
# Function Based View

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

'''
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.error, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
'''