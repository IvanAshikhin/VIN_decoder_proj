from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from decoder.functions import get_car

from .serializers import CarSerializer


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
    def post(self, request) -> Response:
        vin_code = self.request.data.get("vin_code")
        if not vin_code or len(vin_code) != 17:
            return Response(
                {"error": "Invalid VIN code. Must be 17 characters long."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        car = get_car(vin_code)
        if car:
            serialized_car = CarSerializer(car).data
            return Response({"car": serialized_car, "user_id": self.request.user.id})
        else:
            return Response(
                {"error": "Car not found for the provided VIN code"},
                status=status.HTTP_404_NOT_FOUND,
            )
