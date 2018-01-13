from django.shortcuts import render

def Home(request):
    template = 'Home\First.html'
    return render(request, template)

def Contact(request):
    template = 'Home\AboutUs.html'
    return render(request, template)
