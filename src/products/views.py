from django.shortcuts import render
from .models import Pro
from .forms import ProductForm

# Create your views here.
def pro_detail_view(request):
    obj = Pro.objects.get(id=1)
    context = {
         'object' : obj
    }
    return render(request, 'products/product_detail.html', context)  

def pro_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context ={
        'form': form
    }
    return render(request, 'products/product_create.html', context)  


#def pro_crate_view(request):
    #print(request.GET)
    #print(request.POST)
    #my_new_title = request.POST.get('title')
    #Pro.objects.create(title=my_new_title)
    #context={}
    #return render(request, 'products/product_create.html', context)