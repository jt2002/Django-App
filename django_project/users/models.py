from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # CASCADE = If user is deleted, also delete the profile
    #           If profile is deleted, it will not delete the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Image will be uploaded to 'profile_pics' folder
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Override save() method of the model
        # Run save method of the parent class
        super().save(*args, **kwargs)
        # Grap the image and re-size it
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            # Max size
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
