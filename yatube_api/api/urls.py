from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

api_v1_router = DefaultRouter()
api_v1_router.register('posts', views.PostViewSet, basename='post')
api_v1_router.register('groups', views.GroupViewSet, basename='group')

api_v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentViewSet,
                basename='comment')

api_v1_urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(api_v1_router.urls)),
]

urlpatterns = [
    path('v1/', include(api_v1_urlpatterns)),
]
