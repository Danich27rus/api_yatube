from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register(r'^api/v1/posts/(?P<post_id>.+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls))
]
