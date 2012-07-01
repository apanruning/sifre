# -*- coding: utf-8 -*-


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from registration.signals import user_activated
from easy_thumbnails.fields import ThumbnailerImageField

class DefualtUserProfile(models.Model):
    """ """
    user = models.OneToOneField("auth.User")
    email = models.EmailField()
    biopic = models.TextField();
    logo = ThumbnailerImageField(
        upload_to='avatars',
        resize_source=dict(size=(50, 50), crop='smart'),
        null=True, blank=True)
        
    banner = ThumbnailerImageField(
        upload_to='banners',
        resize_source=dict(size=(790, 360), crop='smart'),
        null=True, blank=True)
        
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=12, blank=True)

    class Meta:
        app_label = 'profiles'
    
    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', [self.user.username])
        
    def __unicode__(self):
        return self.institucion
        
@receiver(user_activated, sender=User)
def create_profile(sender, instance, request, **kargs):
    profile = DefualtUserProfile(user=instance, email=instance.email)
    profile.save()
