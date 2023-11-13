from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from vininfo import Vin

from decoder.models import Region, Country, Manufacturer, Brand, Year, Car
from .serializers import CarSerializer


class DecodeVinAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'vin_code': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: CarSerializer(many=False),
            400: "Bad Request - Invalid input or missing vin_code",
        },
        security=[{"JWT": []}],
        operation_summary="Decode VIN Code",
        operation_description="Decode VIN code and return car information.",
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="JWT token in the format 'Bearer <your_token>'.",
                required=True,
            ),
        ],
    )
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
