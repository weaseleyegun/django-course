from django.urls import path, include
from . import views
from .apis import *
from rest_framework.routers import DefaultRouter
from .views import TodoCreateView


router = DefaultRouter()
router.register("", TodoViewSet)

urlpatterns = [
    path("create/", TodoCreateView.as_view()),
    path("", views.todo_main),
    path("list/", views.todo_list),
    path("<int:pk>/", views.todo_detail),
    path("<str:name>/", views.todo_detail_name)
]