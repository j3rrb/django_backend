from django.contrib import admin
from .models import Access, Page, Topic, Pet

admin.site.register([Access, Page, Topic, Pet])
