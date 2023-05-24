from django import urls
from django.urls import path
from .views import HomePageViewSet, NewsViewSet, \
 ScientificEssaysViewSet, InternationalRelations, BooksViewSet, StoriesViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("", HomePageViewSet, basename="home")
router.register("news", NewsViewSet, basename="news")
router.register("scientific_essays", ScientificEssaysViewSet, basename="scientific_essays")
router.register("international_relations", InternationalRelations, basename="international_relations")
router.register("books", BooksViewSet, basename="books")
router.register("stories", StoriesViewSet, basename="stories")



urlpatterns = [

] + router.urls
