from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    thread = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    login = models.ForeignKey(User, on_delete=models.PROTECT)
    op_post = models.TextField()
    thread_date = models.DateTimeField(auto_now=True)
    thread_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.thread


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    post = models.TextField()
    login = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    pic = models.ImageField(null=True, blank=True)



