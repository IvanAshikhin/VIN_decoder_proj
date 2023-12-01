from django.contrib import admin

from decoder.models import Brand, Car, Country, Region, Year, Model


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "brand")
    search_fields = ("name", "code", "brand")
    autocomplete_fields = ["brand"]


@admin.register(Year)
class YearCodeAdmin(admin.ModelAdmin):
    list_display = ("year", "code")
    search_fields = ("year", "code")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("region", "brand", "country", "year", "model")
    search_fields = (
        "region__name",
        "brand__name",
        "country__name",
        "year__year",
        "model__name",
    )
    list_filter = ("region", "brand", "country", "year", "model")
    autocomplete_fields = ["region", "brand", "country", "year", "model"]
    list_select_related = ("region", "brand", "country", "year", "model")
