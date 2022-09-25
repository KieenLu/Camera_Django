from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def document(request):
    context =  {}
    return render(request, "document/document.html", context )