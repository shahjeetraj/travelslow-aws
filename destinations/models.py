from base.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Search(models.Model):
    search_theme = models.CharField(max_length=1000, null=True)
    search_destination = models.CharField(max_length=255, null=True)
    search_custom_query = models.CharField(max_length=1000, null=True)
    search_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="searchBy")
    
    def __str__(self):
        return f"A search was conducted for {self.search_theme}"

class Destination(BaseModel):
    destination_name = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=100)
    destination_info = models.TextField()
    destination_imageURL = models.TextField(null=True)
    destination_imageURL_2 = models.TextField(null=True)
    destination_imageURL_3 = models.TextField(null=True)
    destination_imageURL_4 = models.TextField(null=True)
    destination_imageURL_5 = models.TextField(null=True)
    destination_imageURL_6 = models.TextField(null=True)
    destination_searchID = models.PositiveIntegerField(default=1)
    destination_likes = models.PositiveIntegerField(default=0, null=True)
    
    def __str__(self):
        return f"{self.destination_name}, {self.destination_country}"
    
class Like(models.Model):
    likeUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likedBy")
    likeDestination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="destinationLiked")
    
    def __str__(self) -> str:
        return f"{self.likeDestination} is liked by {self.likeUser}."

class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email