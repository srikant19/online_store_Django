from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
     
       if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            username = request.POST['username']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                   messages.info(request,'username taken')
                   
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email taken')   
                    
                else:
                  user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                  user.save()
                 
                  
            else:
                print('password not matching')
                return redirect('/')
            
       else:
           return render(request,'register.html')
















