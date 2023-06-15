from django.shortcuts import render
from .models import MissingPerson

#These are the codes that allow the routes on the urls.py file to run.  
def MissingPersonsTable (request):
    MissingList = MissingPerson.objects.all()
    context = {
        'persons' : MissingList
    }
    
    return render(request, 'appMP/index.html', context)

# def MissingPersonsTable(request):
#     return render(request, 'appMP/index.html')

def personView (request, personId) :
    data = MissingPerson.objects.filter(
        id=personId
    ).get()
    context = {
        'person': data
    }
    return render(request, 'appMP/person.html', context)