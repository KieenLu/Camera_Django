from django.shortcuts import render

def contact(request):
    context =  {}
    return render(request, "contact/contact.html", context)