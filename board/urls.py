from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("", views.board, name="board"),
    path("pan", views.pan, name="pan"),
    path("pan_write", views.pan_write, name="pan_write"),
    path("pan_insert", views.pan_insert, name="pan_insert"),
    path("pan_view", views.pan_view, name="pan_view"),
    path("pan_edit", views.pan_edit, name="pan_edit"),
    path("pan_update", views.pan_update, name="pan_update"),
    path("pan_delete", views.pan_delete, name="pan_delete"),
]
