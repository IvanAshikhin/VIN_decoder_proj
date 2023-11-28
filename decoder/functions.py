from vininfo import Vin
from vin_decoder_nhtsa.decoder import Vin as VinModel
from .models import Car, Region, Country, Brand, Year, Model


def get_vin_symbol(vin_code: str, start_index: int, end_index: int) -> str:
    return "".join([vin_code[i] for i in range(start_index, end_index)])


def get_country(code: str) -> Country:
    country_code = get_vin_symbol(code, 0, 2)
    existing_country = Country.objects.filter(code=country_code).first()
    if existing_country:
        return existing_country
    return Country.objects.create(code=country_code, name=Vin(code).country)


def get_brand(code: str) -> Brand:
    brand_code = get_vin_symbol(code, 2, 4)
    existing_brand = Brand.objects.filter(code=brand_code).first()
    if existing_brand:
        return existing_brand
    return Brand.objects.create(code=brand_code, name=Vin(code).brand)


def get_model(code: str) -> Model:
    model_code = get_vin_symbol(code, 3, 6)
    existing_model = Model.objects.filter(code=model_code).first()
    if existing_model:
        return existing_model
    vin_info = VinModel(code)
    return Model.objects.create(
        code=model_code, name=vin_info.Model, brand=get_brand(code)
    )


def get_year(code: str) -> Year:
    year_code = get_vin_symbol(code, 9, 11)
    existing_year = Year.objects.filter(code=year_code).first()
    if existing_year:
        return existing_year
    year_value = int(Vin(code).years[0]) if Vin(code).years else None
    year_obj, _ = Year.objects.get_or_create(
        code=year_code, defaults={"year": year_value}
    )
    return year_obj


def create_car(vin_code: str) -> Car:
    country = get_country(vin_code)
    brand = get_brand(vin_code)
    year = get_year(vin_code)
    model = get_model(vin_code)
    region, _ = Region.objects.get_or_create(name=Vin(vin_code).region)
    return Car.objects.create(
        country=country, region=region, brand=brand, year=year, model=model
    )


def get_car(vin_code: str) -> Car:
    try:
        car = Car.objects.get(
            region__name=Vin(vin_code).region,
            country__name=get_country(vin_code),
            brand__name=get_brand(vin_code),
            model__name=get_model(vin_code),
            year__year=get_year(vin_code),
        )
        return car
    except Car.DoesNotExist:
        return create_car(vin_code)
