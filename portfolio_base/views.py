from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'portfolio_base/home.html')
