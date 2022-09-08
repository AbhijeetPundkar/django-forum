from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def room_page(request):
    return render(request, 'room.html')


