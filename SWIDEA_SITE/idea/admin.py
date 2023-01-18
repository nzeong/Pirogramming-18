from django.contrib import admin
from .models import Idea

# Register your models here.
@admin.register(Idea)
class PostAdmin(admin.ModelAdmin):
    pass