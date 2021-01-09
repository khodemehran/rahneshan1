from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .models import formola
from .forms import userinputform

# Create your views here.
def index(request):

    Planet_name = formola.objects.order_by('-created_at')
    context = {
        'Planet_name':Planet_name
    }
    return render(request,'formola/index.html',context)

def userinput(request):
    if request.method == 'POST':
        form = userinputform(request.POST or None)
        esm_object = None
        template_name = None
        #myDict = dict(queryDict.iterlists())
        if form.is_valid():
            #cd = form.cleaned_data
            esm_object = form.cleaned_data['name']
            marhale_roshd = form.cleaned_data['Roshd_date']
            template_name = 'formola/userinput.html'
            try:
                Obj = None
                Obj = formola.objects.get(Q(name__iexact = esm_object) & Q(roshd_time__iexact = marhale_roshd))
                msg = "باموفقیت ثبت شد"
                print(Obj)
                fs = form.save(commit=False)
                fs.user = request.user
                fs.save() 
                template_name = 'formola/userinput.html'
                context={
                    'Obj':Obj,
                    'form':form,
                    'msg':msg,
                        }
                return render(request,template_name,context)

            except formola.DoesNotExist:
                context = {
                'form': form,
                'error':'چنین برنامه ای وجود ندارد',
                            }
                return render(request, template_name, context)
        else:
            form = userinputform()
            template_name = 'formola/userinput.html'
            context = {
                    'Obj':Obj,
                    'form': form,
                    'error': 'ورودی نا معتبر',
                         }
            return render(request, template_name, context)

    else:
        form = userinputform()
        template_name = 'formola/userinput.html'
        context = {
            'form': form,
        }
        return render(request, template_name, context)
