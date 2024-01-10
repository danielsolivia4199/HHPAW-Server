"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpawapi.models import Order

class OrderView(ViewSet):
    """HHPAW orders view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order
        Returns:
            Response -- JSON serialized order
        """
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all items"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'customer_phone', 'order_type', 'is_closed')
