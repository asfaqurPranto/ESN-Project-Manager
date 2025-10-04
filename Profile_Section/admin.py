from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'country', 'profession', 'phone', 'education')
    search_fields = ('user__username', 'city', 'country', 'profession', 'phone', 'education')
    list_filter = ('city', 'country', 'profession')
    ordering = ('-id',)  # newest first
