from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        read_only_fields = ['price']
        fields = ['invoice','id', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']
      