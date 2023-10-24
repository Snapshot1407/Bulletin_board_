from django.contrib import admin
from .models import Ads, Author, Category, Response, AdvertisementCategory

# Register your models here.

admin.site.register(Ads)
admin.site.register(AdvertisementCategory)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Response)