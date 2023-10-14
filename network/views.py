import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count


from .models import *


def index(request):
    allPosts = Post.objects.all().order_by("id").reverse()
    pagination = Paginator(allPosts,10)
    pageNo = request.GET.get('page')
    pagePosts = pagination.get_page(pageNo)
    myLikes = []
    allLikes = Like.objects.all()
    for like in allLikes:
        if request.user == like.likeUser:
            myLikes.append(like.likedPost.id)
    return render(request, "network/index.html", {
        "pagePosts" : pagePosts,
        "myLikes" : myLikes
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def postCreate(request):
    if request.method == "POST":
        postText = request.POST['postText']
        postAuthor = User.objects.get(pk=request.user.id)
        djing = Post(postText=postText, postAuthor=postAuthor)
        djing.save()
        return HttpResponseRedirect(reverse("index"))
    
def profileView(request, user_id):
    user = User.objects.get(pk=user_id)
    userPosts = Post.objects.filter(postAuthor=user).order_by("id").reverse()
    pagination = Paginator(userPosts,10)
    pageNo = request.GET.get('page')
    pagePosts = pagination.get_page(pageNo)
    followers = Follow.objects.filter(profileOwner = user)
    following = Follow.objects.filter(profileFollower = user)
    try:
        followCheck = followers.filter(profileFollower=request.user)
        if len(followCheck) != 0:
            amFollowing = True
        else:
            amFollowing = False
    except:
        amFollowing = False
    allLikes = Like.objects.all()
    profileLikes = 0
    myLikes = []
    for like in allLikes:
        if request.user == like.likeUser:
            myLikes.append(like.likedPost.id)
        if user == like.likedPost.postAuthor:
            profileLikes += 1
    return render(request, "network/profile.html", {
        "pagePosts" : pagePosts,
        "username" : user.username,
        "followers" : followers,
        "following" : following,
        "amFollowing" : amFollowing,
        "profileOwner" : user,
        "myLikes" : myLikes,
        "profileLikes" : profileLikes
    })

def follow(request):
    profileOwner = request.POST['profileOwner']
    profileFollower = request.user
    profileOwnerData = User.objects.get(username=profileOwner)
    f = Follow(profileOwner=profileOwnerData,profileFollower=profileFollower)
    f.save()
    user_id = profileOwnerData.id
    return HttpResponseRedirect(reverse("profileView", kwargs={'user_id':user_id}))

def unfollow(request):
    profileOwner = request.POST['profileOwner']
    profileFollower = request.user.id
    profileOwnerData = User.objects.get(username=profileOwner)
    f = Follow.objects.get(profileOwner=profileOwnerData,profileFollower=profileFollower)
    f.delete()
    user_id = profileOwnerData.id
    return HttpResponseRedirect(reverse("profileView", kwargs={'user_id':user_id}))

def following(request):
    allPosts = Post.objects.all().order_by("id").reverse()
    followList = Follow.objects.filter(profileFollower = request.user)
    followPosts = []
    for post in allPosts:
        for fellow in followList:
            if fellow.profileOwner == post.postAuthor:
                followPosts.append(post)
    pagination = Paginator(followPosts,10)
    pageNo = request.GET.get('page')
    pagePosts = pagination.get_page(pageNo)
    myLikes = []
    allLikes = Like.objects.all()
    for like in allLikes:
        if request.user == like.likeUser:
            myLikes.append(like.likedPost.id)
    return render(request, "network/following.html", {
        "pagePosts" : pagePosts,
        "followList" : followList,
        "myLikes" : myLikes
    })

def search(request):
    searchText = request.GET.get('searchText', '')
    postList = Post.objects.filter(postText__icontains=searchText)
    userList = User.objects.filter(username__icontains=searchText)
    
    pagination = Paginator(postList,10)
    pageNo = request.GET.get('page')
    pagePosts = pagination.get_page(pageNo)
    myLikes = []
    allLikes = Like.objects.all()
    for like in allLikes:
        if request.user == like.likeUser:
            myLikes.append(like.likedPost.id)
    return render(request, "network/search.html", {
        "pagePosts" : pagePosts,
        "userList" : userList,
        "searchText" : searchText,
        "myLikes" : myLikes
    })

@csrf_exempt
@login_required
def postEdit(request, post_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        data = json.loads(request.body)
        post2Edit = Post.objects.get(pk=post_id)
        post2Edit.postText = data['newPostText']
        post2Edit.save()
        return JsonResponse({"message": "djing modified successfully."}, status=201)

@csrf_exempt    
@login_required
def postLike(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        data = json.loads(request.body)
        post_id = data['post_id']
        postLiked = Post.objects.get(pk=post_id)
        userId = request.user.id
        postLikedBy = User.objects.get(pk=userId)
        like = Like(likedPost=postLiked,likeUser=postLikedBy)
        like.save()
        postLiked.postLikes += 1
        postLiked.save()
        return JsonResponse({"message": "djing liked successfully.", "postLike" : postLiked.postLikes}, status=201)

@csrf_exempt    
@login_required
def postUnLike(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        data = json.loads(request.body)
        post_id = data['post_id']
        postLiked = Post.objects.get(pk=post_id)
        userId = request.user.id
        postLikedBy = User.objects.get(pk=userId)
        like = Like.objects.filter(likedPost=postLiked,likeUser=postLikedBy)
        like.delete()
        postLiked.postLikes -= 1
        postLiked.save()
        return JsonResponse({"message": "djing unliked successfully.", "postLike" : postLiked.postLikes}, status=201)