"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from hhpawapi.models import OrderItem, Order, Item

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

    def create(self, request):
        try:
            order = get_object_or_404(Order, pk=request.data["order_id"])
            item = get_object_or_404(Item, pk=request.data["item_id"])          
            order_item = OrderItem.objects.create(order=order, item=item)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
        Handle DELETE requests for a single order item
        Args:
            pk (int): Primary key of the order item to be deleted
        Returns:
            Response -- HTTP status code
        """
        try:
            order_item = get_object_or_404(OrderItem, pk=pk)
            order_item.delete()
            return Response({'message': 'Order item deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item')
        depth = 1
