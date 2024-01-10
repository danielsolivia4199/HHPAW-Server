"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from hhpawapi.models import OrderItem

class OrderItemView(ViewSet):
    """HHPAW order item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order
        Returns:
            Response -- JSON serialized order
        """
        order_item = OrderItem.objects.get(pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all order items"""
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def items_for_order(self, request, pk=None):
        """
        Handle GET requests for order items of a specific order
        Args:
            pk (int): Primary key of the order
        Returns:
            Response -- JSON serialized list of order items for the specified order
        """
        if pk is not None:
            order_items = OrderItem.objects.filter(order_id=pk)
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Order ID is required'}, status=status.HTTP_400_BAD_REQUEST)
class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item')
        depth = 1
