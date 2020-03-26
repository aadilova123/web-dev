from django.shortcuts import render
from django.http.response import JsonResponse
from core.models import Product
# Create your views here.
def product_list(request):
  products = Product.objects.all()
  products_json = [product.to_json() for product in products]
  return JsonResponse(products_json, safe=False)


def product_detail(request,product_id):
    try:
      product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
      return JsonResponse({'error': str(e) })
    return JsonResponse(product.to_json())

