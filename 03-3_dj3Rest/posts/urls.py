from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# PostList, PostDetail, UserList, UserDetail
app_name = "posts"
router = SimpleRouter()
router.register("", PostViewSet, basename="post")
router.register("user", UserViewSet, basename="user")
urlpatterns = router.urls


# URL pattern: ^users/$          URL Name: 'user-list'
# URL pattern: ^users/{pk}/$     URL Name: 'user-detail'
# URL pattern: ^accounts/$       URL Name: 'account-list'
# URL pattern: ^accounts/{pk}/$  URL Name: 'account-detail'


# urlpatterns = [
#     path("api/", PostList.as_view(), name="list"),
#     path("api/<int:pk>", PostDetail.as_view(), name="detail"),
#     path("users/", UserList.as_view(), name="user-list"),
#     path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
# ]

