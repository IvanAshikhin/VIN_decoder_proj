from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Страна")
    code = models.CharField(max_length=4, verbose_name="Код страны")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ["name"]


class Year(models.Model):
    year = models.CharField(max_length=4, verbose_name="Год производства")
    code = models.CharField(max_length=4, verbose_name="Код года производства")

    def __str__(self):
        return f"{self.year}"

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Год"
        ordering = ["year"]


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Бренд")
    code = models.CharField(max_length=4, verbose_name="Код бренда")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"
        ordering = ["name"]


class Model(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Модель")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Бренд"
    )
    code = models.CharField(max_length=4, verbose_name="Код модели")

    def __str__(self):
        return f"{self.name} {self.brand}"

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модель"
        ordering = ["name"]


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name="Регион")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регион"
        ordering = ["name"]


class Car(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True, verbose_name="Регион"
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, verbose_name="Страна"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, verbose_name="Бренд"
    )
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, null=True, verbose_name="Модель"
    )
    year = models.ForeignKey(
        Year, on_delete=models.CASCADE, null=True, verbose_name="Год"
    )

    def __str__(self):
        return f"{self.region} {self.country} {self.brand} {self.model}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобиль"
