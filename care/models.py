from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class Department(models.Model):
    name = models.CharField(max_length=50, blank=True)
    deals_with = models.TextField(blank=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)    
    
    # link to in-built user model
    @receiver(post_save,sender = User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    # end of link

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(blank=True)
    injury = models.CharField(max_length=30, blank=True)
    INJURY_TYPES = (
    ('green','SAFE'),
    ('yellow','MINIMAL INJURY'),
    ('red','SEVERE INJURY'),
    ('black','PASSED'),
)
    admitted = models.BooleanField(blank=True)