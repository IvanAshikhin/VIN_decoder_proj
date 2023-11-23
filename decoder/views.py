from django.shortcuts import render
from .forms import VinDecodeForm
from .models import Car, Region, Country, Manufacturer, Brand, Year, Model
from vininfo import Vin
from vin_decoder_nhtsa.decoder import Vin as vin_model


def new_decode_vin(request, user_id):
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
            vin_decoder_info = vin_model(vin_code)
            model, _ = Model.objects.get_or_create(model=vin_decoder_info.Model)
            brand.model = model
            brand.save()
            year = Year.objects.get_or_create(year=int(vin.years[0]) if vin.years else None)[0]
            car = Car.objects.create(
                vin_code=vin_code,
                region=region,
                country=country,
                manufacturer=manufacturer,
                brand=brand,
                year=year
            )
        return render(request, 'success_template.html', {'car': car, 'user_id': user_id})
    return render(request, 'decode_vin_template.html', {'form': form, 'user_id': user_id})
