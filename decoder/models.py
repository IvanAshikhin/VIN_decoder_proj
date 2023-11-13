# models.py
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=50)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Year(models.Model):
    year = models.PositiveIntegerField()


class Car(models.Model):
    vin_code = models.CharField(max_length=17)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
