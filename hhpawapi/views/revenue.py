"""View module for handling requests about revenue"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpawapi.models import Revenue

class RevenueView(ViewSet):
    """HHPAW orders view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single revenue
        Returns:
            Response -- JSON serialized order
        """
        revenue = Revenue.objects.get(pk=pk)
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all items"""
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations to create a Revenue record

        Returns:
            Response -- JSON serialized Revenue instance
        """
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """
        Handle DELETE requests for a single revenue record
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            revenue = Revenue.objects.get(pk=pk)
            revenue.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Revenue.DoesNotExist:
            return Response({'message': 'Revenue not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)  
class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue
    """
    class Meta:
        model = Revenue
        fields = ('order', 'order_amount', 'tip_amount', 'payment_type', 'date')
