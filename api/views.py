from rest_framework.decorators import api_view
from api.serializers import ProductSerializer
from rest_framework.response import Response
from api.models import ProductTable
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    ''' List of all Product and create new product api'''
    try:
        if request.method=='GET':
            products = ProductTable.objects.all()
            serializer = ProductSerializer(products,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method=='POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(['PUT','GET','DELETE'])    
def update_product(request,pk):
    ''' Edit , Update and Delete a given product using it's unique ID'''
    try:
        product = ProductTable.objects.get(pk=pk)
    except ProductTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(e)
    
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)