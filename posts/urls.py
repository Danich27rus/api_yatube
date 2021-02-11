from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from yatube_api.settings import API_URL_START

from .views import CommentViewSet, PostViewSet

API_VERSION = 'v1'

router = DefaultRouter()
router.register('/posts', PostViewSet,
                basename='posts')
router.register(r'^/posts/(?P<post_id>.+)/comments',
                CommentViewSet,
                basename='posts')

urlpatterns = [
    path(f'{API_URL_START}/{API_VERSION}/api-token-auth/',
         auth_views.obtain_auth_token),
    path(f'{API_URL_START}/{API_VERSION}', include(router.urls))
]
