from django.shortcuts import render,HttpResponse
from .models import SavedForm

# Create your views here.
def home(request):
    return render(request,'home.html')

    
def contact(request):
    if request.method=='POST':
        contact=SavedForm()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return render(request,'message.html')

    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def projects(request):
    return render(request,'projects.html')

def kindergarten(request):
    return render(request,'kindergarten.html')

def minimalist_arch(request):
    return render(request,'minimalist_arch.html')

def classic_cont(request):
    return render(request,'classic_cont.html')

def morico_c(request):
    return render(request,'morico_cafe.html')

def restaurant_hs(request):
    return render(request,'restaurant.html')

'''def form(request):
    if request.method=='POST':
        name=request.POST.get('fname')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data=SavedForm(name=fname,email=email,message=message)
        data.save()
  '''  

'''def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to the database, send an email, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Optionally return a success message or redirect
            return render(request, 'success.html', {'name': name})

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
'''
    