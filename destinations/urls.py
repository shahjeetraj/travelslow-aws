from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("login", views.login_view, name="login"),
path("logout", views.logout_view, name="logout"),
path("register", views.register, name="register"),
path("search", views.search, name="search"),
path("explore", views.explore, name="explore"),
path("viewMore/<int:id>", views.viewMore, name="viewMore"),
path("destSearch/<int:id>", views.destSearch, name="destSearch"),
path("imageSearch/<str:destination_name>", views.imageSearch, name="imageSearch"),
path("singleImageSearch/<str:destination_name>", views.singleImageSearch, name="singleImageSearch"),
path("destView/<str:destination_name>", views.destView, name="destView"),
path("about", views.about, name="about"),
path("contact", views.contact, name="contact"),
path("send_email", views.send_email, name="send_email"),
path("beta", views.beta, name="beta"),
path('subscribe', views.subscribe, name='subscribe'),
]