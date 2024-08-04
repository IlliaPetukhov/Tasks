from django.urls import path

from catalog import views
from catalog.views import HomePageView, AddTask

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tags", views.TagListView.as_view(), name="tags"),
    path("add-task", views.AddTask.as_view(), name="add-task"),
    path("change-status<int:pk>/", views.ChangeStatus.as_view(), name="change-status"),
    path("update-task<int:pk>/", views.UpdateTask.as_view(), name="update-task"),
    path("delete-task<int:pk>/", views.DeleteTask.as_view(), name="delete-task"),
    path("add-tag", views.AddTag.as_view(), name="add-tag"),
    path("update-tag<int:pk>/", views.UpdateTag.as_view(), name="update-tag"),
    path("delete-tag<int:pk>/", views.DeleteTag.as_view(), name="delete-tag"),
]
