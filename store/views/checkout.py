from django.shortcuts import render
from django.views import  View
from store.models.product import  Product

class Checkout(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request , 'checkout.html' , {'products' : products})