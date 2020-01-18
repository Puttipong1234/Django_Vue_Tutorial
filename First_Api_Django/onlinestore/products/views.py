
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# # Create your views here.
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

### end first lesson ###


from .models import Product , Manufacturer
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all() #[0:30]
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name" : product.name,
            "manufacturer": product.manufacturer.name,
            "description":product.description,
            "photo":product.photo.url,
            "price":product.price,
            "shipping_cost": product.shipping_cost,
            "quantity":product.quantity,
        }}
        response = JsonResponse(data)
    
    except Product.DoesNotExist:
        response = JsonResponse(
            {
                'error':{
                    "code":404,
                    "message":"product not found!"
                }
            }, status = 404 )
    
    return response