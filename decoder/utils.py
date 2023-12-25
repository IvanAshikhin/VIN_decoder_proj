from django.db.models import Count, Max
from .models import Car, User, RequestLog


def vin_search_count():
    return Car.objects.annotate(
        total_vin_search_count=Count("requestlog"),
        distinct_user_count=Count("requestlog__user"),
        last_search_date=Max("requestlog__created_at"),
        search_count_by_date=Count("requestlog__created_at", distinct=True),
    )


def user_vin_search_count_with_date():
    queryset = User.objects.annotate(
        total_vin_search_count=Count("requestlog"),
        distinct_car_count=Count("requestlog__car"),
        last_search_date=Max("requestlog__created_at"),
    )

    return queryset


def vin_search_count_with_date():
    queryset = (
        RequestLog.objects.values(
            "vin",
        )
        .annotate(
            search_count_by_date=Count("created_at"),
            distinct_user_count=Count("user", distinct=True),
            last_search_date=Max("created_at"),
        )
        .order_by("-last_search_date")
    )
    return queryset
