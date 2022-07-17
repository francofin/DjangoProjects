from django.shortcuts import get_object_or_404, render
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Can add authentication for views here, if done in settings then all views are protected. 
# Model View Set

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)


'''
# Generic Viewset

class ArticleList(viewsets.GenericViewSet, 
                mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

'''


'''

# Generic API View


class ArticleList(viewsets.ViewSet):

    lookup_field = 'slug'
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)    

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, slug):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, slug=slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def update(self, request, slug):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, slug=slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, slug=slug)
        article.delete()
        return Response(status=status.HTTP_200_OK)
    

'''



    

'''
Generic Classes
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

        
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
'''

'''
# Mixins

class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)    


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class ArticleDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    lookup_field = 'slug'
    

    def get(self, request, slug,  *args, **kwargs):
        return self.retrieve(request, slug=slug)


    def put(self, request, slug,  *args, **kwargs):
        return self.update(request, slug=slug)

    def delete(self, request, slug,  *args, **kwargs):
        return self.destroy(request, slug=slug)

'''


'''
# Class Based Views

class ArticleList(APIView):


    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)        


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    
    def get_object(self, slug):
      
        try:
            article = Article.objects.get(slug=slug)
            return article
        except Article.DoesNotExist():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def put(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = self.get_object(slug)
        article.delete()
        return Response(status=status.HTTP_200_OK)


'''



'''
# Function based views
# Django api browsable option set up
# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)

#         return Response(serializer.data)

#     elif request.method == "POST":
#         # parse requiest
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", 'DELETE'])
# def article_details(request, slug):
    
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         # parse requiest
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         # parse requiest
#         article.delete()
#         return Response(status=status.HTTP_200_OK)

# get and post articles
# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)

#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         # parse requiest
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
    
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         # parse requiest
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         # parse requiest
#         article.delete()
#         return HttpResponse(status=204)

'''


