from django.db import models
#Newly added
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    #that will inharit from the User model containing id,username->email, password, email, first_name, last_name,is_active,
    # ..is_staff, is_superuser, last_login, date_joined
    #we will add additional fields to the Profile model
    profession = models.CharField(max_length=150, null=True, blank=True)
    bio=models.TextField(max_length=300, blank=True,null=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True,default="Bangladesh")
    phone=models.CharField(max_length=15, null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.id)
    

#Signal to create or update the user profile when the User instance is created/updated.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
        #Profile.objects.get_or_create(user=instance) 

