from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("homenew", views.homenew, name="homenew"),
path("login", views.login_view, name="login"),
path("logout", views.logout_view, name="logout"),
path("register", views.register, name="register"),
path("search", views.search, name="search"),
path("searchnew", views.searchnew, name="searchnew"),
path("explore", views.explore, name="explore"),
path("explorenew", views.explorenew, name="explorenew"),
path("destSearch/<int:id>", views.destSearch, name="destSearch"),
path("imageSearch/<str:destination_name>", views.imageSearch, name="imageSearch"),
path("singleImageSearch/<str:destination_name>", views.singleImageSearch, name="singleImageSearch"),
path("destView/<str:destination_name>", views.destView, name="destView"),
path("like/<str:id>", views.like, name="like"),
path("unlike/<str:id>", views.unlike, name="unlike"),
path("about", views.about, name="about"),
path("contact", views.contact, name="contact"),
path("send_email", views.send_email, name="send_email"),
path("beta", views.beta, name="beta"),
path('subscribe', views.subscribe, name='subscribe'),
]