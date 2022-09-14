from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField()
    no_of_likes = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now_add=True,null=True)
    slug = AutoSlugField(populate_from = 'status', unique = True, null = True)

    def __str__(self):
        return self.status

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    comment = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return self.comment

class likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    has_liked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.post)


class replycomment(models.Model):
    initial_comment = models.ForeignKey(comments, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True , null=True)
    reply = models.CharField(max_length=300)

    

