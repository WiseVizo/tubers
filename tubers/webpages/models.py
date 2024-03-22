from django.db import models

# Create your models here.
class Slider(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    contact_link = models.URLField(default="https://www.youtube.com/") 
    def __str__(self):
        return self.heading
    
class OurTeam(models.Model):
    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='team/%Y/%m')
    facebook_link = models.URLField(default="https://www.facebook.com/")
    linkedin_link = models.URLField(default="https://www.linkedin.com/")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
    