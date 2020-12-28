from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import AuthForm
from django.contrib.auth import logout

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        form = AuthForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            #print('ta inja miad')
            if user is not None:
                login(request, user)
                #if 'next' in request.POST:
                    #return redirect(request.POST['next'])
                #else:
                    #redirect('user_data')
                nxt = request.GET.get("next", None)
                url = '/userdata/user_data'
                if nxt is not None:
                    url += '?next=' + nxt
                    return redirect(url)
                else:
                    return redirect('home')

            else:
                return  render(request,'accounts/login.html',{'form':form, 'error':'نام کاربری و رمز عبور مطابقت ندارد'})
        #else:
            #print("ولید نیست")

    else:
        form = AuthForm()
    return  render(request,'accounts/login.html',{'form':form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
    
    