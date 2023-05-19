from django import urls
from django.urls import path
from .views import HomePageViewSet, NewsViewSet, \
CountryImageViewSet, ScientificArticles, InternationalProjects, BooksViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("", HomePageViewSet, basename="home")
router.register("news", NewsViewSet, basename="news")
router.register("countryimage", CountryImageViewSet, basename="image")
router.register("scientific_articles", ScientificArticles, basename="scientific_articles")
router.register("international_projects", InternationalProjects, basename="international_projects")
router.register("books", BooksViewSet, basename="books")


urlpatterns = [

] + router.urls
