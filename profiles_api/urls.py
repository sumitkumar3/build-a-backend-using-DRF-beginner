from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name = 'hello_viewset')
router.register('user-profile-viewset', views.ProfileViewSet, base_name='profile_viewset')
router.register('feed', views.ProfilefeedViewSet, base_name='profile-feed-status')
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('login', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]
