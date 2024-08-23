from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    
    context = {'images': []}
    return render(request, 'products.html')