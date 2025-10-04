from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Project(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.IntegerField()
    completed = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return f"{self.title} ({self.completed}%)"


class Message(models.Model):
    id = models.AutoField(primary_key=True)  # Unique ID
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_messages')
    content = models.TextField()  # To store the message text
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set time and date when created

    def __str__(self):
        return f"Message {self.id} from {self.sender.username} in project {self.project.title}"