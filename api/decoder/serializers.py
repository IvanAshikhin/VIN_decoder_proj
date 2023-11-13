from rest_framework import serializers


class RegionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class ManufacturerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField(min_value=0)


class CarSerializer(serializers.Serializer):
    vin_code = serializers.CharField(max_length=17)
    region = RegionSerializer()
    country = CountrySerializer()
    manufacturer = ManufacturerSerializer()
    brand = BrandSerializer()
    year = YearSerializer()
