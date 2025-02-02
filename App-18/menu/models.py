from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("main_course", "Main Course"),
    ("sides", "Sides"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=50)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal



