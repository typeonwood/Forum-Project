from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    def __str__(self) -> str:
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_added = models.DateTimeField(auto_now_add=True)
    locked = models.BooleanField(default=False)
    content = models.TextField(max_length=10000)
    media_link = models.TextField(max_length=5000, blank=True)
    def __str__(self) -> str:
        return self.title + ' - ' + str(self.user.username)
        
class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000)
    def __str__(self) -> str:
        return str(self.user.username) + ' - ' + str(self.date_time_added)

class ThreadVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    upvote = models.BooleanField()

class ReplyVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    upvote = models.BooleanField()