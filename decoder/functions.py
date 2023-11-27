from .models import Car, Region, Country, Brand, Year, Model, Code
from vininfo import Vin
from vin_decoder_nhtsa.decoder import Vin as vin_model


def get_vin_symbol(vin_code, start_index, end_index):
    return "".join([vin_code[i] for i in range(start_index, end_index)])


def get_country(code):
    country_code = get_vin_symbol(code, 0, 2)
    existing_country = Country.objects.filter(code__code=country_code).first()
    if existing_country:
        return existing_country
    country_code, _ = Code.objects.get_or_create(code=country_code)
    return Country.objects.create(code=country_code, name=Vin(code).country)


def get_brand(code):
    brand_code = get_vin_symbol(code, 2, 4)
    existing_brand = Model.objects.filter(code__code=brand_code).first()
    if existing_brand:
        return existing_brand
    brand_code, _ = Code.objects.get_or_create(code=brand_code)
    return Brand.objects.create(code=brand_code, name=Vin(code).brand)


def get_model(code):
    model_code = get_vin_symbol(code, 3, 6)
    existing_model = Model.objects.filter(code__code=model_code).first()
    if existing_model:
        return existing_model
    vin_info = vin_model(code)
    model_code, _ = Code.objects.get_or_create(code=model_code)
    return Model.objects.create(code=model_code, name=vin_info.Model, brand=get_brand(code))


def get_year(code):
    year_code = get_vin_symbol(code, 9, 11)
    existing_year = Year.objects.filter(code__code=year_code).first()
    if existing_year:
        return existing_year
    year_value = int(Vin(code).years[0]) if Vin(code).years else None
    year_code, _ = Code.objects.get_or_create(code=year_code)
    year_obj, _ = Year.objects.get_or_create(code=year_code, defaults={'year': year_value})
    return year_obj


def decode_vin(vin_code):
    country = get_country(vin_code)
    brand = get_brand(vin_code)
    year = get_year(vin_code)
    model = get_model(vin_code)
    region, _ = Region.objects.get_or_create(name=Vin(vin_code).region)
    car = Car.objects.create(country=country, region=region, brand=brand, year=year, model=model)
    return car
