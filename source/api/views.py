import json

from django.core.serializers import serialize, deserialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers = json.loads(request.body)
            first_number = numbers['A']
            second_number = numbers['B']
            if type(first_number) == int and type(second_number) == int:
                total = first_number + second_number
                return JsonResponse({'answer': total})
            else:
                response = JsonResponse({'error': 'Need integer'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers = json.loads(request.body)
            first_number = numbers['A']
            second_number = numbers['B']
            if type(first_number) == int and type(second_number) == int:
                total = first_number - second_number
                return JsonResponse({'answer': total})
            else:
                response = JsonResponse({'error': 'Need integer'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response

@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers = json.loads(request.body)
            first_number = numbers['A']
            second_number = numbers['B']
            if type(first_number) == int and type(second_number) == int:
                total = first_number * second_number
                return JsonResponse({'answer': total})
            else:
                response = JsonResponse({'error': 'Need integer'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response

@csrf_exempt
def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers = json.loads(request.body)
            first_number = numbers['A']
            second_number = numbers['B']
            if type(first_number) == int and type(second_number) == int:
                total = first_number / second_number
                return JsonResponse({'answer': total})
            else:
                response = JsonResponse({'error': 'Need integer'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response
