from django.contrib import admin
from .models import Access, Page, Topic

admin.site.register([Access, Page, Topic])
