from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PostSerializer, BookSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
import json
from django.utils.translation import get_language, activate, gettext
from . import utils
from .models import Posts, BooksModel, Product
# Create your views here.


class HomePageViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        
        queryset = Posts.objects.all()
        search_query = request.query_params.get('q', '')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(text__contains=search_query))
        
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class NewsViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Yangiliklar" if language == 'uz' else "News"        
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SampleViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Yangiliklar" if language == 'uz' else "News"        
        queryset = Posts.objects.filter(category__contains=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class ArticleViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Articles" if language == 'en' else "Maqolalar"
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ScientificEssaysViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Scientific_Essays" if language == 'en' else "Ilmiy_tezislar"
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
     

class BooksViewSet(ViewSet):
    def list(self, request):
        queryset = BooksModel.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)     
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class InternationalRelations(ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE
        query_word = "International_Relations" if language == 'en' else "Xalqaro_munosabatlar"
        queryset = Posts.objects.filter(category=query_word)
        
        search_query = self.request.query_params.get('q', '')
        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, self.request)
        if paginated_queryset is not None:
            return paginated_queryset
        return queryset
    
class MagazinesViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Magazines" if language == 'en' else "Jurnallar"
        queryset = Posts.objects.filter(category=query_word)
        
        search_query = request.query_params.get('q', '')
        
        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    

class PhotoViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Photo" if language == 'en' else "Foto_lavhalar"
        queryset = Posts.objects.filter(category=query_word)
        
        search_query = request.query_params.get('q', '')
        
        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PoetryViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Poetry" if language == 'en' else "Sheriyat"
        queryset = Posts.objects.filter(category=query_word)
        
        search_query = request.query_params.get('q', '')
        
        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
class StoriesViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Stories" if language == 'en' else "Hikoyalar"        
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    



