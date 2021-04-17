from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    OTHERS = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS,'Others'),
    )
    user = models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
    college = models.CharField(max_length=256, blank=True)
    #birthdate = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)



    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
'''
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
'''
