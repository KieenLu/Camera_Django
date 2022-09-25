from django.shortcuts import render

# Create your views here.
def API(request):
    context =  {}
    return render(request, "API/API.html", context)