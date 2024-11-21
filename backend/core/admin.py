from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin, UserAdmin
from .models import User, Phrases

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Phrases)
class PhrasesAdmin(admin.ModelAdmin):
    list_display = ('portuguesePhrase', 'translatedPhrase')

# Register your models here.
