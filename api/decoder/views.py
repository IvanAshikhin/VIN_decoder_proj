from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  AllowAny
from vininfo import Vin

from decoder.models import Region, Country, Manufacturer, Brand, Year, Car
from .serializers import CarSerializer


class DecodeVinAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        vin_code = request.data.get('vin_code', None)

        if not vin_code:
            return Response({'error': 'Vin code is required'}, status=status.HTTP_400_BAD_REQUEST)

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

        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
