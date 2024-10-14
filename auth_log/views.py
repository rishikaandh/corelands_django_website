from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate,login, logout


# Create your views here.
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.warning(request,"password not matching")
            return render(request, 'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"email already taken")
                return render(request, 'signup.html')
        except Exception as identifier:
            pass
        user= User.objects.create_user(email, email, password)    #(name in html, cloumn name in user table, column name in user table)
        #user,is_active=False
        user.save()   
        return render(request,'login.html')
    return render(request, 'signup.html')








def handlelogin(request):
        if request.method== "POST":
            username = request.POST['email']
            userpassword= request.POST['password']
            myuser= authenticate(username=username, password=userpassword)

            if myuser is not None:
                login(request,myuser)
                messages.success(request,'login success')
                return redirect('/')
            else:
                messages.error(request,'invalid credentials')
                return render(request, 'login.html')

    
        return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"logout successful")

    return render(request, 'login.html')
