from django.shortcuts import render
from .forms import VinDecodeForm
from .models import Car, Region, Country, Manufacturer, Brand, Year
from vininfo import Vin


def decode_vin(request):
    form = VinDecodeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        vin_code = form.cleaned_data['vin_code']
        vin = Vin(vin_code)
        try:
            car = Car.objects.get(vin_code=vin_code)
        except Car.DoesNotExist:
            region, _ = Region.objects.get_or_create(name=vin.region)
            country, _ = Country.objects.get_or_create(name=vin.country)
            manufacturer, _ = Manufacturer.objects.get_or_create(name=vin.manufacturer)
            brand, _ = Brand.objects.get_or_create(name=vin.brand)
            year = Year.objects.get_or_create(year=int(vin.years[0]) if vin.years else None)[0]

            car = Car.objects.create(
                vin_code=vin_code,
                region=region,
                country=country,
                manufacturer=manufacturer,
                brand=brand,
                year=year
            )

        return render(request, 'success_template.html', {'car': car})

    return render(request, 'decode_vin_template.html', {'form': form})