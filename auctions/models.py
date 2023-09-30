from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName
    
class Bid(models.Model):
    bid = models.FloatField(default=0)
    bidUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

    def __str__(self):
        return f"{self.bidUser} has bid {self.bid}."
    
class Listing(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1048)
    imageUrl = models.CharField(max_length=2096)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="wishlist")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="commentingUser")
    listing = models.ForeignKey(Listing, blank=True, null=True, on_delete=models.CASCADE, related_name="commentListing")
    commentMessage = models.CharField(max_length=1048)

    def __str__(self) -> str:
        return f"{self.author} commented: {self.commentMessage}"