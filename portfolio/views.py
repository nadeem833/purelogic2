from django.shortcuts import render , redirect
from django.contrib import messages
from portfolio.models import Contact


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num') 
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,decrption=fdesc)
        query.save()
        messages.success(request,'Thank you for contacting , We will get back you soon.!')


        return redirect('/contact')

    return render(request, 'contact.html')    

    
def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')    