
# Create your views here.
from django.shortcuts import render

# Create your views here.
def price(request):
    context =  {}
    return render(request, "price/price.html", context )