from django.db import models

# Create your models here.
class Slider(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading