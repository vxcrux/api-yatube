from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentViewSet,
                basename='comment')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
