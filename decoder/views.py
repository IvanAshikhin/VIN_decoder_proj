"""
Необходимо декодировать вин без запроса
Если нет одного и более поля - которые не заполнены
Произвести поиск в других базах и пополнить их в свою базу, дабы в последующем использовать локальную базу данных
Тест: Произвести инкремент последних 3 цифр
        # try:
        #     result = decode_vin()
        # except DoesNotExist:
        #     result = parsing_vin()
        # if result == None:
        # # ERROR RESPONSE
        # return Response(result, status=200)
"""

from django.shortcuts import render
from .forms import VinDecodeForm
from .functions import decode_and_create_car


def new_decode_vin_view(request, user_id):
    form = VinDecodeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        vin_code = form.cleaned_data['vin_code']
        car = decode_and_create_car(vin_code)
        return render(request, 'success_template.html', {'car': car, 'user_id': user_id})
    return render(request, 'decode_vin_template.html', {'form': form, 'user_id': user_id})
