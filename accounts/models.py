from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    verify_email = models.EmailField()
    birth_date = models.DateField(null=True, blank=True)
    bio = RichTextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True,
                               default='default-user-profile.png')
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country_of_residence = models.CharField(max_length=30, blank=True)
    favorite_animal = models.CharField(max_length=30, blank=True)
    hobby = models.CharField(max_length=30, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



