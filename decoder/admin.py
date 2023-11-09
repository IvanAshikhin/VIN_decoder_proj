from django.contrib import admin
from .models import Country, CountryCode, ProductionYear, YearCode, Mark, MarkCode, Model


@admin.register(CountryCode)
class CountryCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(YearCode)
class YearCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(ProductionYear)
class ProductionYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'code')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(MarkCode)
class MarkCode(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'mark', 'code')
