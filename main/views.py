from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PostSerializer, BookSerializer, VideoSerializer, CertificateSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
import json
from django.http import JsonResponse
from rest_framework import generics
from django.utils.translation import get_language, activate, gettext
from . import utils
from rest_framework import filters
from .models import Posts, BooksModel, VideoModel, CertificateModel
# Create your views here.


class HomePageModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
        
    def get_queryset(self):
            queryset = self.queryset
            search_q = self.request.query_params.get('q')
            if search_q:
                queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
            return queryset 
        
class NewsModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
        
    def get_queryset(self):
            queryset = self.queryset.filter(category="Yangiliklar")
            search_q = self.request.query_params.get('q')
            if search_q:
                queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
            return queryset 

class ArticleModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get']
    search_fields = ['title', 'text']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Maqolalar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset 
    

class ScientificArticlesViewSet(ViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Ilmiy_Maqolalar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset 
     

class BooksModelViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = BooksModel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
        
    def get_queryset(self):
        queryset = self.queryset
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset 
    

class InternationalRelationsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset.filter(category="Xalqaro_munosabatlar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset  
    
class MagazinesModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Jurnallar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset   
       

   
class PhotoModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Foto_lavhalar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset   
    
class PoetryModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Sheriyat")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset
    
class StoriesModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Hikoyalar")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset

class OcherklarModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = self.queryset.filter(category="Yol_ocherklari")
        search_q = self.request.query_params.get('q')
        if search_q:
            queryset = queryset.filter(Q(title__contains=search_q) | Q(text__contains=search_q))
        return queryset  
        
class VideoModelViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = VideoModel.objects.all()
    http_method_names = ['get']

class CertificateModelViewSet(ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = CertificateModel.objects.all()
    http_method_names = ['get']
        
class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello")
    

def getRoutes(request):
    routes = [
        '',
        '/news',
        '/news/<str:pk>/',
        '/articles',
        '/articles/<str:pk>/',
        '/scientific_essays',
        '/scientific_essays/<str:pk>/',
        '/international_relations',
        '/international_relations/<str:pk>/',
        '/books',
        '/books/<str:pk>/',
        '/stories',
        '/stories/<str:pk>/',
        '/videos',
        '/videos/<str:pk',
        '/poetry',
        '/poetry/<str:pk>/',
        '/photos',
        '/photos/<str:pk>/',
        '/magazines',
        '/magazines/<str:pk>/',
    ]
    return JsonResponse(routes, safe=False)