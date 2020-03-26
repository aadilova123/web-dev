from django.shortcuts import render

from django.http.response import HttpResponse,JsonResponse
# Create your views here.

# products = []
# for i in range(1,5):
#   products.append(
#     {
#       'id':i,
#       'name':f'product{i}',
#       'price':i*1000
#     }
#   )
#
products = [
  {
      'id':i,
      'name':f'product{i}',
      'price':i*1000
  } for i in range(1,5)
]

def hello(request):
  return HttpResponse('hello msg')

def product_list(request):
  return JsonResponse(products, safe=False)

def product_detail(request,product_id):
  for product in products:
    if product['id'] == product_id:
      return JsonResponse(product)

  return JsonResponse({'error':'product does not exist'})
