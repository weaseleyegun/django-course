from django.urls import path
from . import views
from .apis import *

urlpatterns = [
    path("create/", TodoCreateAPI.as_view()),
    path("list_api/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetripeveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
    path("", views.todo_main),
    path("list/", views.todo_list),
    path("<int:pk>/", views.todo_detail),
    path("<str:name>/", views.todo_detail_name)

]

