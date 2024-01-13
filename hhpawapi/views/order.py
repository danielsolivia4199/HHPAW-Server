"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpawapi.models import Order, Employee


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

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized order instance
        """
        employee = Employee.objects.get(uid=request.data["employee"])

        order = Order.objects.create(
            customer_name=request.data["customerName"],
            customer_email=request.data["customerEmail"],
            customer_phone=request.data["customerPhone"],
            order_type=request.data["orderType"],
            is_closed=request.data["isClosed"],
            employee=employee,
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for order

        Returns:
            Response -- Empty body with 204 status code
        """
        order = Order.objects.get(pk=pk)
        order.customer_name = request.data["customerName"]
        order.customer_email = request.data["customerEmail"]
        order.customer_phone = request.data["customerPhone"]
        order.order_type = request.data["orderType"]

        order.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_email',
                  'customer_phone', 'order_type', 'is_closed')
