from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Project_Section.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','tags', 'creater', 'created_at', 'deadline', 'completed','description')
    list_filter = ('creater', 'completed')
    search_fields = ('title', 'description', 'creater__username')
    list_editable = ('title', 'completed','deadline', 'tags','description')
    ordering = ('-id',)  # newest first


from Project_Section.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'project', 'content', 'created_at')
    list_filter = ('sender', 'project')
    search_fields = ('content', 'sender__username', 'project__title')
    ordering = ('-created_at',)  # newest first