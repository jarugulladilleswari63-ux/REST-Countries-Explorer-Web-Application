from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    data = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,currencies,flags").json()
    if request.method == "POST":
        a = request.POST.get('a')
        data = requests.get(f"https://restcountries.com/v3.1/name/{a}").json()
        return render(request,'display.html',{'data':data})
    return render(request,'index.html',{'data':data})