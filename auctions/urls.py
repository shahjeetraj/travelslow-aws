from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("category_wise_listing/<str:category>/", views.category_wise_listing, name="category_wise_listing"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("my_listings/", views.my_listings, name="my_listings"),
    path("wishlistAdd/<int:id>", views.wishlistAdd, name="wishlistAdd"),
    path("wishlistRemove/<int:id>", views.wishlistRemove, name="wishlistRemove"),
    path("wishlistDisplay/", views.wishlistDisplay, name="wishlistDisplay"),
    path("commentAdd/<int:id>", views.commentAdd, name="commentAdd"),
    path("bidAdd/<int:id>", views.bidAdd, name="bidAdd"),
    path("auctionClose/<int:id>", views.auctionClose, name="auctionClose"),
    path("myBid/", views.myBid, name="myBid"),
]
