from django.shortcuts import render, redirect
from .models import formola
from .forms import userinput

# Create your views here.
def index(request):

    Planet_name = formola.objects.order_by('-created_at')
    context = {
        'Planet_name':Planet_name
    }
    return render(request,'formola/index.html',context)

def userinput(request):

    form = userinput(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save() 
            cd = form.cleaned_data
            
    else:
        context = {
            'form': form,
            'error': 'خطایی پیش آمده است',
        }
        return render(request, template_name, context)
