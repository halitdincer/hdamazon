from django.shortcuts import render

from .models import Product

def index(request):
    
    products = Product.objects.all()

    response = {
            'products' : products,
    }

    return render(request,'index.html',response)    

def product_view(request,p_id):
 
    sproduct = Product.objects.get(id=p_id)

    response = {
            'sproduct' : sproduct,
    }

    return render(request,'view.html',response)
