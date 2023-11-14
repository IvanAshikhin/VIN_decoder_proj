from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from vininfo import Vin
from decoder.models import Region, Country, Manufacturer, Brand, Year, Car
from .serializers import CarSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample


class DecodeVinAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer

    @extend_schema(
        request={
            "application/json": {
                "example": {"vin_code": "string"},
                "schema": {
                    "type": "object",
                    "properties": {
                        "vin_code": {"type": "string"},
                    },
                    "required": ["vin_code"],
                },
            }
        },
        responses={200: CarSerializer},
    )
    def post(self, request, *args, **kwargs):
        vin_code = request.data.get('vin_code')

        if not vin_code:
            return Response({'error': 'Vin code is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            car = Car.objects.get(vin_code=vin_code)
        except Car.DoesNotExist:
            vin = Vin(vin_code)
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

        serializer = self.serializer_class(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
