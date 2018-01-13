from django.shortcuts import render

def Home(request):
    template = 'Home\First.html'
    return render(request, template)

def AboutPage(request):
    template = 'Home\Logg.html'
    return render(request, template)

def Contact(request):
    template = 'Home\Contact.html'
    return render(request, template)
