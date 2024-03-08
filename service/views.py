from django.shortcuts import render
from forms import Registration


# Create your views here.
def Register(request):
    form = Registration()
    return render(request,'register.html',{'form':form})
