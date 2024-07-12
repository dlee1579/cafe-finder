from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from cafe.models import Cafe

# Create your models here.
class ReviewIntegerField(models.IntegerField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
        kwargs['validators'] = validators
        kwargs['null'] = False
        kwargs['blank'] = False
        super().__init__(*args, **kwargs)
    

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    coffee_quality = ReviewIntegerField()
    comfortability = ReviewIntegerField()
    atmosphere = ReviewIntegerField()
    quietness = ReviewIntegerField()
    cleanliness = ReviewIntegerField()
    
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=250, blank=True)
    
    def __str__(self) -> str:
        if not self.author:
            return "anonymous - {}: {}".format(self.cafe.name, self.title)
        return "{} - {}: {}".format(self.author.username, self.cafe.name, self.title)