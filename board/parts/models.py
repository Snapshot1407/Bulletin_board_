from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_category(self):
        return self.name


    def __str__(self):
        return self.name


class Ads(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through="AdvertisementCategory")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


    text = models.TextField(unique=True)


    def __str__(self):
        return self.title

class Response(models.Model):
    advertisement = models.ForeignKey(Ads, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)


class AdvertisementCategory(models.Model):
    post = models.ForeignKey(Ads, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)