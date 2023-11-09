from django.db import models


class CountryCode(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class YearCode(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code


class ProductionYear(models.Model):
    year = models.IntegerField(max_length=5)
    code = models.ForeignKey(YearCode, on_delete=models.CASCADE)


class MarkCode(models.Model):
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class Mark(models.Model):
    name = models.CharField(max_length=50)
    code = models.ForeignKey(MarkCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    code = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.name
