
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("postCreate", views.postCreate, name="postCreate"),
    path("profileView/<int:user_id>", views.profileView, name="profileView"),
    path("follow", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("search", views.search, name="search"),
    path("postEdit/<int:post_id>", views.postEdit, name="postEdit"),
    path("postLike", views.postLike, name="postLike"),
    path("postUnLike", views.postUnLike, name="postUnLike"),
]
