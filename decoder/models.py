from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)


class Year(models.Model):
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=4)


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=4)


class Model(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=4)


class Region(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
