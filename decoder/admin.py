from django.contrib import admin

from decoder.models import Region, Country, Year, Brand, Car


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Year)
class YearCodeAdmin(admin.ModelAdmin):
    list_display = ("year",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("region", "brand", "country", "year")
