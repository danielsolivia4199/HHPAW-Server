"""View module for handling requests about orders"""
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
class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue
    """
    class Meta:
        model = Revenue
        fields = ('order', 'order_amount', 'tip_amount', 'payment_type', 'date')
