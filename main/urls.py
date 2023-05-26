from django import urls
from django.urls import path, include
from .views import HomePageModelViewSet, NewsModelViewSet,  \
 ScientificEssaysViewSet, InternationalRelationsViewSet, BooksModelViewSet, StoriesModelViewSet 
from rest_framework.routers import DefaultRouter
from .views import ArticleModelViewSet, VideoModelViewSet, PoetryModelViewSet, PhotoModelViewSet, \
        MagazinesModelViewSet

app_name = 'main'

router = DefaultRouter()
router.register("home", HomePageModelViewSet, basename='home')
router.register("news", NewsModelViewSet, basename='news')
router.register("articles", ArticleModelViewSet, basename="articles")
router.register("scientific_essays", ScientificEssaysViewSet, basename="scientific_essays")
router.register("international_relations", InternationalRelationsViewSet, basename="international_relations")
router.register("books", BooksModelViewSet, basename="books")
router.register("stories", StoriesModelViewSet, basename="stories")
router.register("videos", VideoModelViewSet, basename="videos")
router.register("poetry", PoetryModelViewSet, basename="poetry")
router.register("photos", PhotoModelViewSet, basename="photo")
router.register("magazines", MagazinesModelViewSet, basename="magzines")

urlpatterns = [
        path('', include(router.urls))
] 