from django.shortcuts import render,HttpResponse
from .forms import LoginForm

def login_views(request):
    real_password="abcd"
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']
            if real_password == password:
                request.session["password"] = "abcd"
                return HttpResponse('login successful')
            else:
                return HttpResponse('login not succesful')
        else:
            form=LoginForm()
            return render(request,"one.html",{'form':form})
    else:
        form=LoginForm()
        return render(request,"one.html",{'form':form})