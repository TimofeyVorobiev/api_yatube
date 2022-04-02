from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostsViewSet, GroupsViewSet, CommentsViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostsViewSet, basename='posts')
router_v1.register('groups', GroupsViewSet, basename='groups')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
