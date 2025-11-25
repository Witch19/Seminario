from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Warehouse
from ..serializers.warehouse import WarehouseSerializer

@api_view(['GET'])
def warehouse_get_list(request):
    qs = Warehouse.objects.all()
    q = (request.query_params.get('q') or '').strip()
    if q:
        qs = qs.filter(
            Q(code__icontains=q) |
            Q(name__icontains=q) |
            Q(address__icontains=q) |
            Q(city__icontains=q)
        )
        data = WarehouseSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def warehouse_post_create(request):
    serializer = WarehouseSerializer(data=request.data)
    if serializer.is_valid():
        warehouse=serializer.save()
        return Response(
            warehouseserializer(warehouse).data, 
            status=status.HHTP_200_OK)
    return Response(
        serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
    )