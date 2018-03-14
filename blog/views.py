from django.shortcuts import render
from django.views import generic
from .models import Author
# Create your views here.

class AuthorListView(generic.ListView):
    model = Author

def index(request):
    return render(request,'index.html')