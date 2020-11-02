from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'Authorisation/index.html')

class UserFormView(View):
    form_class=UserForm
    template_name='Authorisation/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('Authorisation:login')
        
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    #use formset and refer sibtc
    form_class=LoginForm
    template_name='Authorisation/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        user_type_input=request.POST['user_type']
        print(email)
        print(password)
        user=authenticate(email=email,password=password)
        # user_details=Authorisation.objects.get(pk=request.user.id)
        # user_type=user_details.user_type
        print(user)
        if user is not None:
            if user.is_active:
                print(user)
                login(request,user)
                return redirect('Inventory:index')
            else:
                return render(request, 'Authorisation/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Authorisation/login.html', {'form':form,'error_message': 'Invalid login'})
        

class LogoutView(View):
    form_class=LoginForm
    template_name='Authorisation/login.html'
    def get(self,request):
        form=self.form_class(None)
        logout(request)
        return redirect(reverse('Authorisation:login'))

