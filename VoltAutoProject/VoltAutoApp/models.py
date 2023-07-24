from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Automaker(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    automaker = models.ForeignKey(Automaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=200)
    automaker = models.ForeignKey(Automaker, on_delete=models.CASCADE, null=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    battery_capacity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    range_per_charge = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    image = models.ImageField(upload_to="cars/", default="default.jpg")
    year = models.IntegerField(null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author.username
