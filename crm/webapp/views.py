from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,RecordForm,UploadForm,UpdateForm 
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
from django.views import View


# homepage
class Home(View):
    template_name='webapp/index.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
#register
class Register(View):
    template_name='webapp/register.html'
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        context={'form':form}
        return render(request,self.template_name,context=context)
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created successfully")
            return redirect("Login")
        context={'form':form}
        return render(request,self.template_name,context=context)
    
#login
class Login(View):
    template_name='webapp/login.html'
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        context={'form':form}
        return render(request,self.template_name,context=context)
    def post(self,request,*args,**kwargs):
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
        context={'form':form}
        return render(request,self.template_name,context=context)

#dashboard
class dashboard(View):
    template_name='webapp/dashboard.html'
    @login_required(login_url='login')
    def get(self,request,*args,**kwargs):
        records=Record.objects.all()
        context={'records':records}
        return render(request,self.template_name,context=context)