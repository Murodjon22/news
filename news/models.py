import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

class Post(models.Model):
    image = models.ImageField(upload_to='image/', blank=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
