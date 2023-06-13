from django.shortcuts import render

# Create your views here.

def MissingPersonsTable(request):
    return render(request, 'appMP/index.html')