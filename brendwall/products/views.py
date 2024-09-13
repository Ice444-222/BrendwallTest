from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    http_method_names = ['get', 'post']

    def retrieve(self, request, *args, **kwargs):
        return Response({"detail": "Method 'GET' not allowed for individual product."}, status=405)

    def list(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)