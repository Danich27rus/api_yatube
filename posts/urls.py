from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

API_VERSION = 'v1'

file = open("api_prefix.txt", 'r')
content = file.read()
print(content)
file.close()

router = DefaultRouter()
router.register('posts', PostViewSet,
                basename='posts')
router.register(r'^posts/(?P<post_id>.+)/comments',
                CommentViewSet,
                basename='posts')

urlpatterns = [
    path(f'{content}/{API_VERSION}/api-token-auth/',
         auth_views.obtain_auth_token),
    path(f'{content}/{API_VERSION}/', include(router.urls))
]
