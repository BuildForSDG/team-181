from django.shortcuts import render
from api.serializers import FamersInfoSerializers, ProductsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.http import JsonResponse
from farmers.models import FarmerDetails, Products
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def get_farmers_info(request):
    # farmers_info = FarmerDetails.objects.all()
    # serializer = FamersInfoSerializers(farmers_info, many=True)
    # return JsonResponse({'Info': serializer.data}, safe=False, status= status.HTTP_200_OK)

    if request.method == "GET":
        farmers_info = FarmerDetails.objects.all()
        serializer = FamersInfoSerializers(farmers_info, many=True)
        return JsonResponse({'Info': serializer.data}, safe=False, status= status.HTTP_200_OK)
        print("It is working")

# Create products as an authenticated user.
@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_products(request):
    product = Products.objects.all()
    if request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_products(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK) 


# Get a specific product by an ID
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny, ))
def get_products_by_id(request, pk):
    try:
         products = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return JsonResponse({'msg': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
         serializer = ProductsSerializer(products)
         return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)