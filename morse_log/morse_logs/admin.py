from django.contrib import admin
"""Remember to add the import of the class as well"""
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)