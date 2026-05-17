from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


# Car Model Model
class CarModel(models.Model):

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        default=2023
    )

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"