from django.shortcuts import render
from .forms import Planet_Form
from .models import PlanetData


# Create your views here.


def user_data(request):
    form = Planet_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            fs = form.save(commit=False)
            Category = form.cleaned_data.get('Category')
            Name = form.cleaned_data.get('Name')
            Age_Stirng = form.cleaned_data.get('Age_string')
            Age_Numberic = form.cleaned_data.get('Age_Numberic')
            Weather = form.cleaned_data.get('Weather')
            Water = form.cleaned_data.get('Water')
            Area = form.cleaned_data.get('Area')
            #model
            PlanetData = PlanetData()
            PlanetData.Age_Numberic = Age_Numberic
            PlanetData.Age_Stirng = Age_Stirng
            PlanetData.Area = Area
            PlanetData.Weather = Weather
            PlanetData.Category = Category
            PlanetData.Name = Name 
            PlanetData.Water = Water
            if Age_Stirng and Age_Numberic:
                context = {
                            'form':form,
                            'error':'you can not fill both field ',
                           }
                return render(request, 'your template', context)

            else:
                PlanetData.save()
                fs.save()
                context = {
                    'form':form,
                    'error':'your data have been saved',
                }

                return render(request, 'Userdata/data.html', context)

    else:
        context = {
            'form':form
                  }
        return render(request, 'Userdata/data.html', context)



            

            


            
