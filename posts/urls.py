from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from rest_framework.authtoken import views as auth_views

API_URL_START = 'api'
API_VERSION = 'v1'

router = DefaultRouter()
router.register(f'{API_URL_START}/{API_VERSION}/posts', PostViewSet,
                basename='posts')
router.register(fr'^{API_URL_START}/'
                fr'{API_VERSION}/posts/(?P<post_id>.+)/comments',
                CommentViewSet,
                basename='posts')

urlpatterns = [
    path(f'{API_URL_START}/{API_VERSION}api-token-auth/',
         auth_views.obtain_auth_token),
    path('', include(router.urls))
]
