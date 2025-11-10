from django.shortcuts import render,get_object_or_404
from. models import Product
# View to render the product page
def product_list(request):
    uploads = Product.objects.all()
    return render(request,'men.html',{'uploads':uploads})

def product_details(request,product_id):
    upload=get_object_or_404(Product,id=product_id)   
    return render(request, 'product_details.html', {'upload': upload})

# Create your views here.
