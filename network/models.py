from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    postText = models.CharField(max_length=255)
    postAuthor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    postDate = models.DateTimeField(auto_now_add=True)
    postLikes = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f"{self.postAuthor} posted on {self.postDate.strftime('%B %d %Y, %H:%M:%S')}"
    
class Follow(models.Model):
    profileOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    profileFollower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profileFollower} started following {self.profileOwner} on {self.followDate.strftime('%B %d %Y, %H:%M:%S')}"

class Like(models.Model):
    likedPost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    likeUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likedBy")
    likeDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.likeUser} liked {self.likedPost.id} on {self.likeDate.strftime('%B %d %Y, %H:%M:%S')}"