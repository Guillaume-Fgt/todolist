from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

htmx_urlpatterns = [
    path("add_task/", views.add_task, name="add_task"),
    path("delete_task/<int:pk>", views.delete_task, name="delete_task"),
]

urlpatterns += htmx_urlpatterns
