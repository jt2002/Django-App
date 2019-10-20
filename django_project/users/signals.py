# A signal that gets fired after the object is saved
from django.db.models.signals import post_save
# User is the sender, i.e. send the signal
from django.contrib.auth.models import User
# Receiver - A function that gets the signal and performs some tasks
from django.dispatch import receiver
# We will create a profile in a function
from .models import Profile

# When a User is saved, send the signal (post_save)
# The signal (post_save) will be received by receiver
# The receiver is the create_profile function,
#   which takes those arguments
#   that post_save signal passes to it
# One of those is instance of the User,
#   and one of those is created
# If that user is created, create a profile object
#   with the user = instance of the User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save profile whenever the user profile is saved
# **kwargs accepts any key-word arguments into the function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
