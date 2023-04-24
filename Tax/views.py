from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
tax_rate = 0.15
def index(request):
    return HttpResponse('this is a site to calculate tax')

def tax(request, num):
    num = num + (num * tax_rate)
    return HttpResponse(f'the number after we add the tax {num}')

def taxrate(request):  
    return render(request, "Tax/taxrate.html",{"Taxrate":tax_rate})

