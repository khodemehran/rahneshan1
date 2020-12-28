from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Planet_Form, ContactForm
from .models import PlanetData, Contact



# Create your views here.

@login_required(login_url='login')
def user_data(request):
    if request.method == 'POST':
        form = Planet_Form(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.User = request.user
            fs.save()
            context = {
                'form':form,
                'error':'اطلاعات شما با موفقیت ذخیره شد',
            }
            return render(request, 'Userdata/data.html', context)
    else:
        form = Planet_Form()
        context = {
            'form':form
                  }
        return render(request, 'Userdata/data.html', context)



            

            

def about(request):
    return render(request, 'Userdata/about.html')
            

def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            context = {
                'form':form,
                'error':'با موفقیت ثبت شد'
            }
            return render(request, 'Userdata/contact.html',context)



        
    
    return render(request, 'Userdata/contact.html',{'form':form})


def home(request):
    return render(request, 'Userdata/home.html')