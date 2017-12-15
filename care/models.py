from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/', default='/media/profile/user.svg', null=True)
    
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

class Cause(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Physician(models.Model):
    specialty = models.CharField(max_length=50, blank=True)
    deals_with = models.ManyToManyField(Cause, blank=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    identifier = models.UUIDField(max_length=8, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(blank=True, null=True)
    injury = models.CharField(max_length=30, blank=True)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)
    INJURY_TYPES = (
    ('green','SAFE'),
    ('yellow','MINIMAL INJURY'),
    ('red','SEVERE INJURY'),
    ('black','DECEASED'),
)
    blood_type = models.CharField(max_length=5, blank=True)
    weight = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    occupation = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=30, choices=INJURY_TYPES, blank=True)
    date_admitted = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
