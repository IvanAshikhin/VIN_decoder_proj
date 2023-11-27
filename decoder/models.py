from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=4)


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, null=True, blank=True)


class Year(models.Model):
    year = models.CharField(max_length=4)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, null=True, blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, null=True, blank=True)


class Model(models.Model):
    name = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    code = models.ForeignKey(Code, on_delete=models.CASCADE, null=True, blank=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, null=True)


class Region(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
