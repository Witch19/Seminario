from django.shortcuts import render
from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def area_triangulo(request):
    try:
        base = float(request.data.get('base'))
        height = float(request.data.get('height'))
        area = 0.5 * base * height
        return Response({'area': area}, status=status.HTTP_200_OK)
    except (TypeError, ValueError):
        return Response(
            {'error': 'Invalid input. Please provide numeric values for base and height.'},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def tabla_multiplicar(request, numero):
    try:
        num = int(request.query_params.get('numero',0))
        tabla = {i: num * i for i in range(1, 11)}
        return Response({'tabla': tabla}, status=status.HTTP_200_OK)
    except ValueError:
        return Response(
            {'error': 'Invalid input. Please provide a valid integer.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
def contar_mayores(request):
    try:
        numbers = request.data.get('numbers', [])
        limit = request.data.get('limite ', 0)
        threshold = float(request.data.get('threshold'))
        count = sum(1 for number in numbers if float(number) > threshold)
        return Response({'count': count}, status=status.HTTP_200_OK)
    except (TypeError, ValueError):
        return Response(
            {'error': 'Invalid input. Please provide a list of numbers and a numeric threshold.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
def exponente(request):
    try:
        base = float(request.data.get('base'))
        exponent = float(request.data.get('exponent'))
        result = base ** exponent
        return Response({'result': result}, status=status.HTTP_200_OK)
    except (TypeError, ValueError):
        return Response(
            {'error': 'Invalid input. Please provide numeric values for base and exponent.'},
            status=status.HTTP_400_BAD_REQUEST
        )