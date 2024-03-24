from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):
    CREW_CHOICES = (
        ('solo', 'solo'),
        ('small', 'small (3-5 people)'),
        ('large', 'large (5+ people)'),
    )
    CAMERA_CHOICES = (
    ('dslr', 'DSLR'),
    ('mirrorless', 'Mirrorless'),
    ('compact', 'Compact'),
    ('action', 'Action'),
    ('drone', 'Drone'),
    ('other', 'Other'),
    )
    CATEGORY_CHOICES = (
    ('tech', 'Tech'),
    ('gaming', 'Gaming'),
    ('vlogs', 'Vlogs'),
    ('cooking', 'Cooking'),
    ('music', 'Music'),
    ('fitness', 'Fitness'),
    ('travel', 'Travel'),
    ('other', 'Other'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    crew = models.CharField(max_length=255, choices=CREW_CHOICES)
    camera_type = models.CharField(max_length=255, choices=CAMERA_CHOICES)
    sub_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    description = RichTextField()
    channel_link = models.URLField(default="https://www.youtube.com")

    age = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()

    photo = models.ImageField(upload_to='youtubers/%Y/%m/%d')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
