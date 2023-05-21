from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PostSerializer, SuggestionSerializer, BookSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
import json

from . import utils
from .models import Posts, SuggestionModel, BooksModel
# Create your views here.


class HomePageViewSet(ViewSet):
    def list(self, request):
        
        language = request.LANGUAGE_CODE
        
        queryset = Posts.objects.all()
        search_query = request.query_params.get('q', '')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(text__contains=search_query))
        section_keywords = utils.pair_language(language)
        
        news_obj = list(queryset.filter(category=section_keywords[0]).order_by("-created_at")[:5].values())
        article_obj = list(queryset.filter(category=section_keywords[1]).order_by("-created_at")[:5].values())
        country_image_obj = list(queryset.filter(category=section_keywords[2]).order_by("created_at")[:5].values())
        scientific_articles = list(queryset.filter(category=section_keywords[3]).order_by("created_at")[:5].values())
        book_obj = list(queryset.filter(category=section_keywords[4]).order_by("-created_at")[:5])
        international_projects = list(queryset.filter(category=section_keywords[5]).order_by("-created_at")[:5].values())
        data = {
            "news_obj":news_obj, "article_obj":article_obj, "country_image_obj":country_image_obj,
            "scientific_articles":scientific_articles, "book_obj":book_obj, 
            "international_projects":international_projects
        }
        return Response(data)

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
        queryset = Posts.objects.filter(category__contains=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            print(page)
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
            print(page)
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    

class CountryImageViewSet(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "CountryImage" if language == 'en' else "Mamlakat_Imiji"
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            print(page)
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
            print(page)
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ScientificArticles(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "Scientific_Articles" if language == 'en' else "Ilmiy_Maqolalar"
        queryset = Posts.objects.filter(category=query_word)
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            print(page)
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

class InternationalProjects(ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        language = request.LANGUAGE_CODE
        query_word = "International_Projects" if language == 'en' else "Xalqaro_Loyihalar"
        queryset = Posts.objects.filter(category=query_word)
        
        search_query = request.query_params.get('q', '')
        
        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
       
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            print(page)
            serializer = PostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SuggestionViewSet(ViewSet):    
    def list(self, request):
        suggestions = SuggestionModel.objects.all()
        serializer = SuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = SuggestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



