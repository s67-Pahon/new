from django.db import models

# Create your models here.

class List(models.Model):
    pass

class Item(models.Model):
    PRIORITY_HIGH = "H"
    PRIORITY_MED = "M"
    PRIORITY_LOW = "L"

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "High"),
        (PRIORITY_MED, "Medium"),
        (PRIORITY_LOW, "Low"),
    ]

    text = models.TextField(default="")
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_MED,
    )