from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PostSerializer, SuggestionSerializer
from django.db.models import Q
import json
from .models import Posts, SuggestionModel
# Create your views here.

class HomePageViewSet(ViewSet):
    def list(self, request):
        queryset = Posts.objects.all()
        search_query = request.query_params.get('q', '')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(text__contains=search_query))

        news_obj = list(queryset.filter(category="NEWS").order_by("-created_at")[:5].values())
        article_obj = list(queryset.filter(category="ARTICLES").order_by("-created_at")[:5].values())
        country_image_obj = list(queryset.filter(category="COUNTRYIMAGE").order_by("created_at")[:5].values())
        scientific_articles = list(queryset.filter(category="SCIENTIFIC_ARTICLES").order_by("created_at")[:5].values())
        book_obj = list(queryset.filter(category="BOOKS").order_by("-created_at")[:5])
        international_projects = list(queryset.filter(category="INTERNATIONAL_PROJECTS").order_by("-created_at")[:5].values())
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
    def list(self, request):
        queryset = Posts.objects.filter(category="NEWS")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    

class CountryImageViewSet(ViewSet):
    def list(self, request):
        queryset = Posts.objects.filter(category="COUNTRYIMAGE")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data) 

class ArticleViewSet(ViewSet):
    def list(self, request):
        queryset = Posts.objects.filter(category="ARTICLES")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)        
    


class ScientificArticles(ViewSet):
    def list(self, request):
        queryset = Posts.objects.filter(category="SCIENTIFIC_ARTICLES")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)        

class BooksViewSet(ViewSet):
    def list(self, request):
        queryset = Posts.objects.filter(category="BOOKS")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)        


class InternationalProjects(ViewSet):
    def list(self, request):
        queryset = Posts.objects.filter(category="INTERNATIONAL_PROJECTS")
        search_query = request.query_params.get('q', '')

        if search_query:
            queryset = queryset.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
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



