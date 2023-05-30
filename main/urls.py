from django import urls
from django.urls import path, include
from .views import HomePageModelViewSet, NewsModelViewSet,  \
 ScientificArticlesViewSet, InternationalRelationsViewSet, BooksModelViewSet, StoriesModelViewSet 
from rest_framework.routers import DefaultRouter
from .views import ArticleModelViewSet, VideoModelViewSet, PoetryModelViewSet, PhotoModelViewSet, \
        MagazinesModelViewSet, OcherklarModelViewSet, CertificateModelViewSet

app_name = 'main'

router = DefaultRouter()
router.register("home", HomePageModelViewSet, basename='home')
router.register("news", NewsModelViewSet, basename='news')
router.register("articles", ArticleModelViewSet, basename="articles")
router.register("scientific_articles", ScientificArticlesViewSet, basename="scientific_articles")
router.register("international_relations", InternationalRelationsViewSet, basename="international_relations")
router.register("books", BooksModelViewSet, basename="books")
router.register("stories", StoriesModelViewSet, basename="stories")
router.register("videos", VideoModelViewSet, basename="videos")
router.register("poetry", PoetryModelViewSet, basename="poetry")
router.register("photos", PhotoModelViewSet, basename="photo")
router.register("magazines", MagazinesModelViewSet, basename="magzines")
router.register("ocherklar", OcherklarModelViewSet, basename="ocherklar")
router.register("certificates", CertificateModelViewSet, basename="certificates")

urlpatterns = [
        path('', include(router.urls))
] 