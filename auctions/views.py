from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

def home(request):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    return render(request, "auctions/home.html",{
        "categories" : categories
    })

def about(request):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    return render(request, "auctions/about.html",{
        "categories" : categories
    })

def index(request):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    active_list = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html",{
        "active_list" : active_list,
        "categories" : categories
    })

def category_wise_listing(request, category):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    cat_name = Category.objects.get(categoryName=category)
    active_list = Listing.objects.filter(isActive=True, category=cat_name)
    return render(request, "auctions/category-wise.html",{
        "category" : cat_name,
        "active_list" : active_list,    
        "categories" : categories
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        if username == "" or email == "" or password == "":
            return render(request, "auctions/register.html", {
                "message": "All Fields are mandatory!."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, "auctions/create.html",{
            "categories" : categories
        })
    else:
        title = request.POST.get('title')
        description = request.POST.get('description')
        imageurl = request.POST.get('imageUrl')
        price = request.POST.get('price')
        category = request.POST.get("category")
        list_user = request.user
        cat_val = Category.objects.get(categoryName=category)

        bid = Bid(bid=price, bidUser=list_user)
        bid.save()
        new_listing = Listing(title=title, description=description, imageUrl=imageurl, price=bid, category=cat_val, owner=list_user)
        new_listing.save()

        return HttpResponseRedirect(reverse(my_listings))
    
def listing(request, id):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    list_data = Listing.objects.get(pk=id)
    currentUser = request.user
    allComments = Comment.objects.filter(listing=list_data)
    if currentUser in list_data.watchlist.all(): 
        isWishlisted = True
    else:
        isWishlisted = False
    return render(request, "auctions/listing.html",{
        "listing" : list_data,
        "isWishlisted" : isWishlisted,
        "allComments" : allComments,
        "categories" : categories
    })

def my_listings(request):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    list_data = Listing.objects.filter(owner=request.user)
    return render(request, "auctions/my_listings.html",{
        "list_data" : list_data,
        "categories" : categories
    })


def wishlistAdd(request, id):
    list_data = Listing.objects.get(pk=id)
    currentUser = request.user
    list_data.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def wishlistRemove(request, id):
    list_data = Listing.objects.get(pk=id)
    currentUser = request.user
    list_data.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def wishlistDisplay(request):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    currentUser = request.user
    user_wishlist = currentUser.wishlist.all()
    return render(request, "auctions/wishlist.html",{
        "user_wishlist" : user_wishlist,
        "categories" : categories
    })

def commentAdd(request, id):
    currentUser = request.user
    list_data = Listing.objects.get(pk=id)
    currentComment = request.POST.get("comment")
    newComment = Comment(author=currentUser, listing=list_data, commentMessage=currentComment)
    newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def bidAdd(request, id):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    list_data = Listing.objects.get(pk=id)
    currentBid = request.POST.get("bid")
    allComments = Comment.objects.filter(listing=list_data)
    if int(currentBid) > int(list_data.price.bid):
        updateBid = Bid(bidUser=request.user, bid=currentBid)
        updateBid.save()
        list_data.price = updateBid
        list_data.save()
        return render(request, "auctions/listing.html",{
            "listing" : list_data,
            "message" : "Bid updated successfully",
            "allComments" : allComments,
            "categories" : categories
        })
    else:
        return render(request, "auctions/listing.html",{
            "listing" : list_data,
            "message" : "Update Failed since Bid is lesser than previous/minimum bid !",
            "allComments" : allComments,
            "categories" : categories
        })
    
def auctionClose(request, id):
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    list_data = Listing.objects.get(pk=id)
    list_data.isActive = False
    list_data.save()
    allComments = Comment.objects.filter(listing=list_data)
    return render(request, "auctions/listing.html",{
            "listing" : list_data,
            "message" : "Auction is closed successfully",
            "allComments" : allComments,
            "categories" : categories
        })

def myBid(request):
    currentUser = request.user
    categories_all = Category.objects.all()
    categories = []
    for cat in categories_all:
        if len(Listing.objects.filter(isActive=True, category=cat)) > 0:
            categories.append(cat)
    inactive_list = Listing.objects.filter(isActive=False)
    my_winning_bids = []
    for list in inactive_list:
        if list.price.bidUser == currentUser:
            my_winning_bids.append(list)
    return render(request, "auctions/myBid.html",{
        "my_winning_bids" : my_winning_bids,    
        "categories" : categories
    })