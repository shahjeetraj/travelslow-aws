import asyncio
import json
import requests
import openai
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from asgiref.sync import async_to_sync, sync_to_async
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


from .models import *

# Create your views here.

def home(request):
    destinations = Destination.objects.order_by('destination_searchID').reverse()[:14]
    return render(request, "destinations/home.html", {
        "destinations" : destinations
    })

@require_POST
def search(request):
    searchList = []

    searchVal1 = request.POST.get('adventure')
    if searchVal1 != None:
        searchList.append(searchVal1)
    searchVal2 = request.POST.get('beach')
    if searchVal2 != None:
        searchList.append(searchVal2)
    searchVal3 = request.POST.get('history')
    if searchVal3 != None:
        searchList.append(searchVal3)
    searchVal4 = request.POST.get('culture')
    if searchVal4 != None:
        searchList.append(searchVal4)
    searchVal5 = request.POST.get('island')
    if searchVal5 != None:
        searchList.append(searchVal5)
    searchVal6 = request.POST.get('road')
    if searchVal6 != None:
        searchList.append(searchVal6)
    searchVal7 = request.POST.get('luxury')
    if searchVal7 != None:
        searchList.append(searchVal7)
    searchVal8 = request.POST.get('cruise')
    if searchVal8 != None:
        searchList.append(searchVal8)
    searchVal9 = request.POST.get('community')
    if searchVal9 != None:
        searchList.append(searchVal9)
    if len(searchList) != 0:
        search_theme = searchList
    else:
        search_theme = None
    searchVal10 = request.POST.get('dreamText')
    if searchVal10 != None:
        search_custom_query = searchVal10
    else:
        search_custom_query = None
    searchVal11 = request.POST.get('countryList')
    if searchVal11 != None:
        search_destination = searchVal11
    else:
        search_destination = None
    if not request.user.is_authenticated:
        search_user = None
        
    else:
        search_user = request.user
        

    if search_theme == None and search_destination == None and search_custom_query == None:
        message = "No search terms provided."
    else:
        if search_user == None:
            searchGroup = Search(search_theme=search_theme, search_destination=search_destination, search_custom_query=search_custom_query)
        else:
            searchGroup = Search(search_theme=search_theme, search_destination=search_destination, search_custom_query=search_custom_query, search_user=search_user)
        searchGroup.save()
        message = "Please wait while we search the best destinations for you."

    return render(request, "destinations/search.html",{
        "searchGroup" : searchGroup,
        "message" : message
    })
    
def explore(request):
    if not request.user.is_authenticated:
        search_user = None
    else:
        search_user = request.user
    if search_user == None:
        searchGroup = Search(search_theme="", search_destination="", search_custom_query="")
    else:
        searchGroup = Search(search_theme="", search_destination="", search_custom_query="", search_user=search_user)
    searchGroup.save()
    message = "Please allow a minute for AI to render The Best Destinations.."
    return render(request, "destinations/search.html", {
        "searchGroup" : searchGroup,
        "message": message
    })

async def destSearch(request, id):
    searchItem = await get_search_item(id)
    searchList = [searchItem.search_theme, searchItem.search_destination, searchItem.search_custom_query]
    openai.api_key = settings.OPENAI_API_KEY
    if len(searchList) != 0:
        temp_expr = (str(item) for item in searchList)
        separator = ', '
        searchMessage = separator.join(temp_expr)
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant, who will search the internet for 5 holiday destinations that are less crowded and make sure that the same destination is not repeated every time a similar search is made. The response should be in JSON with array called 'destinations' and fields with headers 'destination_name', 'destination_country' and 'destination_information. The field destination_name not to contain country name, it should either be a city, state or area."},
                {"role": "user", "content": ("Please provide destinations ideal for " + searchMessage)}
                ]
            )
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant, who will search the internet for 5 holiday destinations that are less crowded and make sure that the same destination is not repeated every time a similar search is made. The response should be in JSON with array called 'destinations' and fields with headers 'destination_name', 'destination_country' and 'destination_information. The field destination_name not to contain country name, it should either be a city, state or area."},
                {"role": "user", "content": "Please provide 5 random destinations which are not crowded"}
                ]
            )
    
    # parse completion:
    parsedCompletion = json.loads(completion['choices'][0]['message']['content'])
    parsedCompletion["destination_searchID"] = id
    print(parsedCompletion)
    # Create a list of tasks to save destinations and fetch images
    await saveDest(parsedCompletion)
        
    return JsonResponse({"response":parsedCompletion}, status=200)

@sync_to_async
def get_search_item(id):
    return Search.objects.get(pk=id)

@sync_to_async
def save_dest_item(parsedData):
    destination_name = parsedData["destination_name"]
    destination_country = parsedData["destination_country"]
    destination_info = parsedData["destination_info"]
    destination_searchID = parsedData["destination_searchID"]
    destination_imageURL = parsedData["destination_image_urls"][0]
    destination_imageURL_2 = parsedData["destination_image_urls"][1]
    destination_imageURL_3 = parsedData["destination_image_urls"][2]
    destination_imageURL_4 = parsedData["destination_image_urls"][3]
    destination_imageURL_5 = parsedData["destination_image_urls"][4]
    destination_imageURL_6 = parsedData["destination_image_urls"][5]
    destAdd = Destination(
        destination_name=destination_name,
        destination_country=destination_country,
        destination_info=destination_info,
        destination_searchID=destination_searchID,
        destination_imageURL=destination_imageURL,
        destination_imageURL_2=destination_imageURL_2,
        destination_imageURL_3=destination_imageURL_3,
        destination_imageURL_4=destination_imageURL_4,
        destination_imageURL_5=destination_imageURL_5,
        destination_imageURL_6=destination_imageURL_6
        )
    destAdd.save()
    print(f"{destination_name}, {destination_country} destination is added")


# def destSearch(request, id):
#     print(id)
#     print("reached here")
#     parsedCompletion = {
#         'destinations': [
#             {
#                 'destination_name': 'Boracay',
#                 'destination_country': 'Philippines',
#                 'destination_information': 'Boracay is a small island in the Philippines known for its white sand beaches, crystal clear waters, and vibrant nightlife. It offers a perfect beach getaway with a range of water sports and activities, as well as plenty of relaxation options.'
#             },
#             {
#                 'destination_name': 'Zanzibar',
#                 'destination_country': 'Tanzania',
#                 'destination_information': 'Zanzibar is an archipelago off the coast of Tanzania in East Africa. It is famous for its pristine beaches, turquoise waters, and rich cultural heritage. The island provides a blend of history, culture, and relaxation, making it an ideal beach getaway destination.'
#             },
#             # Add more destinations here
#         ]
#     }

#     return JsonResponse({"response":parsedCompletion}, status=200)
    
# def imageSearch(request, destination_name):
#     try:
#         # Make a request to Google Places API using your API key
#         google_api_key = settings.YOUR_GOOGLE_API_KEY
#         place_search_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={google_api_key}&input={destination_name}&inputtype=textquery"

#         place_images_response = requests.get(place_search_url)

#         if place_images_response.status_code == 200:
#             images_data = place_images_response.json()
#             print(images_data)
#             # Process the images_data and return relevant data to the frontend
#             # You can send the image URLs and other information in the response
#             return JsonResponse(images_data)
#         else:
#             return JsonResponse({"error": "Google Places API request failed"}, status=500)

#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

async def saveDest(parsedCompletion):
    try:
        for i in range(len(parsedCompletion["destinations"])):
            destination_name=parsedCompletion["destinations"][i]["destination_name"]
            if "," in destination_name:
                destination_name_split = destination_name.split(", ")
                destination_name = destination_name_split[0]
            if "'" in destination_name:
                destination_name = destination_name.replace("'","")
            destination_country=parsedCompletion["destinations"][i]["destination_country"]
            destination_info=parsedCompletion["destinations"][i]["destination_information"]
            destination_searchID=parsedCompletion["destination_searchID"]
            destWithCntry = destination_name+", "+destination_country
            parsedData = {"destination_name":destination_name,"destination_country":destination_country,"destination_info":destination_info,"destination_searchID":destination_searchID}
            try:
                image_urls = imageSearch(destWithCntry)
                parsedData["destination_image_urls"] = image_urls
                print ("image urls saved successfully in parsedData")
            except Exception as e:
                print(e)
            await save_dest_item(parsedData)
    except Exception as e:
        print(f"{e} not processed splitting destinations data")
        return JsonResponse({"error": str(e)}, status=500)

def imageSearch(destination_name):
    try:
        # Replace 'YOUR_UNSPLASH_API_KEY' with your actual Unsplash API key
        unsplash_api_key = settings.YOUR_UNSPLASH_API_KEY

        # You can customize the parameters like orientation, per_page, etc. as needed
        params = {
            "query": destination_name,
            "client_id": unsplash_api_key,
            "per_page": 6,  # Number of results you want
        }
        print(params)
        # Make a request to Unsplash's search photos API
        unsplash_url = "https://api.unsplash.com/search/photos/"
        unsplash_response = requests.get(unsplash_url, params=params)

        if unsplash_response.status_code == 200:
            images_data = unsplash_response.json()
            print(images_data)
            image_URL_list = []
            if len(images_data["results"]) >= 6:
                # Get only the image url and store in destination_imageURL
                for i in range(6):
                    image_URL_list.append(images_data["results"][i]["urls"]["regular"])
            else:
                stock_travel_images = [
                    "https://images.unsplash.com/photo-1678393813297-c8ee5e1c5327",
                    "https://images.unsplash.com/photo-1540270776932-e72e7c2d11cd",
                    "https://images.unsplash.com/photo-1532279248814-7683684d7184",
                    "https://images.unsplash.com/photo-1690912887220-817575eccc4b",
                    "https://images.unsplash.com/photo-1541583109612-1186fd836a5c",
                    "https://images.unsplash.com/photo-1551478578-633e748b8822",
                    ]
                for i in range(len(images_data)):
                    image_URL_list.append(images_data["results"][i]["urls"]["regular"])
                stock_photos_required = 6-len(images_data["results"])
                for c in range(stock_photos_required):
                    image_URL_list.append(stock_travel_images["results"][c]["urls"]["regular"])
            print(image_URL_list)
            # You can send the image URLs and other information in the response
            return image_URL_list
        else:
            print("Unsplash API request failed")
            return JsonResponse({"error": "Unsplash API request failed"}, status=500)

    except Exception as e:
        print(f"{e} error occurred")
        return JsonResponse({"error": str(e)}, status=500)
    
def about(request):
    return render(request, "destinations/about.html")

def contact(request):
    return render(request, "destinations/contact.html")

def beta(request):
    return render(request, "destinations/register4beta.html")

def destView(request, destination_name):
    dest = Destination.objects.filter(destination_name=destination_name)
    destForPage = dest.latest('destination_searchID')
    likes = Like.objects.filter(likeDestination=destForPage).count()

    if isinstance(request.user, AnonymousUser):
        # User is not logged in
        liked = False
    else:
        # User is logged in
        liked = Like.objects.filter(likeDestination=destForPage, likeUser=request.user).exists()

    return render(request, "destinations/destination.html", {
        "destDetails": destForPage,
        "likes": likes,
        "liked": liked
    })

async def singleImageSearch(request, destination_name):
    try:
        # Replace 'YOUR_UNSPLASH_API_KEY' with your actual Unsplash API key
        unsplash_api_key = settings.YOUR_UNSPLASH_API_KEY

        # You can customize the parameters like orientation, per_page, etc. as needed
        params = {
            "query": destination_name,
            "client_id": unsplash_api_key,
            "per_page": 1,  # Number of results you want
        }
        print(params)
        # Make a request to Unsplash's search photos API
        unsplash_url = "https://api.unsplash.com/search/photos/"
        unsplash_response = requests.get(unsplash_url, params=params)

        if unsplash_response.status_code == 200:
            images_data = unsplash_response.json()
            print(images_data)
            if len(images_data["results"]) != 0:
                # Get only the image url and store in destination_imageURL
                image_URL = images_data["results"][0]["urls"]["regular"]
            else:
                image_URL = "https://images.unsplash.com/photo-1678393813297-c8ee5e1c5327"
            print(image_URL)                
            # You can send the image URLs and other information in the response
            return JsonResponse({"response":image_URL},status=200)
        else:
            return JsonResponse({"error": "Unsplash API request failed"}, status=500)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


require_POST
def register(request):
    username = request.POST["username"]
    email = request.POST["emailid"]
    password = request.POST["password"]
    # Attempt to create new user
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except IntegrityError:
        return render(request, "destinations/register4beta.html", {
            "message": "Username already taken."
        })
    login(request, user)
    return render(request, "destinations/register4beta.html", {
            "message": "User signed up successfully."
        })

require_POST
def login_view(request):
    # Attempt to sign user in
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    # Check if authentication successful
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "destinations/register4beta.html", {
            "message": "Invalid username and/or password."
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def send_email(request):
    subject = request.POST.get("subject", "")
    sender = request.POST.get("sender", "")
    message = sender+request.POST.get("message", "")
    from_email = settings.EMAIL_HOST_USER
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["travelslow2023@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("contact")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def like(request, id):
    liked_destination = Destination.objects.get(pk=id)
    liked_user = request.user
    like_model_instance = Like()
    like_model_instance.likeDestination = liked_destination
    like_model_instance.likeUser = liked_user
    like_model_instance.save()
    likes = liked_destination.destination_likes
    likes = len(Like.objects.filter(likeDestination=liked_destination))
    if Like.objects.filter(likeDestination=liked_destination,likeUser=request.user):
        liked = True
    else:
        liked = False
    return JsonResponse({"likes": likes, "liked": liked}, status=201)
    
@login_required
def unlike(request, id):
    liked_destination = Destination.objects.get(pk=id)
    liked_user = request.user
    like_model_instance = Like.objects.get(likeDestination = liked_destination, likeUser = liked_user)
    like_model_instance.delete()
    likes = liked_destination.destination_likes
    likes = len(Like.objects.filter(likeDestination=liked_destination))
    if Like.objects.filter(likeDestination=liked_destination,likeUser=request.user):
        liked = True
    else:
        liked = False
    return JsonResponse({"likes": likes, "liked": liked}, status=201)