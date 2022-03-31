from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostsViewSet, GroupsViewSet, CommentsViewSet

router = DefaultRouter()
router.register('posts', PostsViewSet, basename="posts")
router.register('groups', GroupsViewSet, basename="groups")
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comment')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
