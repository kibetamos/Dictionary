from django.shortcuts import render
# Create your views here.
#from pyDictionary import pyDictionary
from PyDictionary import PyDictionary

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)

    context = {
        'meaning': meaning,
        'synonym': synonym,
        'antonym': antonym,
    }

    return render(request, 'word.html', context)
