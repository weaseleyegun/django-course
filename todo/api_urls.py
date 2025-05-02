from django.urls import path, include
from . import views
from .apis import *
from rest_framework.routers import DefaultRouter
from .views import TodoCreateView


router = DefaultRouter()
router.register("", TodoViewSet)

urlpatterns = [
    path("viewsets/", include(router.urls)),
    path("generics/create/", TodoGenericsCreateAPI.as_view()),
    path("generics/list/", TodoGenericsListAPI.as_view()),
    path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDestoryAPI.as_view()),
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view()),
    path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view()),
    path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view()),
    # path("create/", TodoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetripeveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
]

