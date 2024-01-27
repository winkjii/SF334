from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request) :
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742206 nattida yiamsanoi views!')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id
    }

    return render(request, 'index.html', context = context_data)

def item_view1(request):
    
    return render(request, 'homepage.html')

def item_view2(request):
    
    return render(request, 'category.html')

def item_view3(request):
    
    return render(request, 'productpage.html')

def item_view4(request):
    
    return render(request, 'checkoutpage.html')

def item_view5(request):
    
    return render(request, 'contactpage.html')
