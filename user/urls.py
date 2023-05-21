from django.urls import path
from .views import SignUpView, LoginViewSet, LogoutViewSet, MyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")
router.register("", MyViewSet, basename="choice")

urlpatterns = [
    path("singup/", SignUpView.as_view(), name='singup')
]
urlpatterns += router.urls
