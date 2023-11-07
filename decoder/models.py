from django.db import models


class CountryCode(models.Model):
    code = models.CharField(max_length=2)


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class YearCode(models.Model):
    code = models.CharField(max_length=2)


class ProductionYear(models.Model):
    year = models.IntegerField()
    code = models.ForeignKey(YearCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.year


class Mark(models.Model):
    name = models.CharField(max_length=30)


class CarMark(models.Model):
    name = models.CharField(max_length=50)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
