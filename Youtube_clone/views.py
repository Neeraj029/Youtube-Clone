from django.http import HttpResponse
from django.shortcuts import render,redirect
from main.models import Video
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    videos = Video.objects.all()
    # print(request.user.email)
    # print(dir(request.user))
    return render(template_name = 'index.html' , request = request , context={"video":videos , 'users':request.user})

def loginPage(request):
    return render(request, 'signin.html', {})

def handleLogin(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        print(username , password)

    user = authenticate(request , username = username , password = password)

    if user is not None:
        login(request , user)

    messages.success(request, "Logged-in successfully!")
    return redirect('/')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged-out successfully!")
    return redirect('/')

def signupPage(request):
    return render(request, 'signup.html')

def handleSignup(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    emali = request.POST['uname'] + '@gmail.com'
    pword = request.POST['password']
    print(fname , lname , uname , emali , pword)

    if fname != '' and lname != '' and uname != '' and emali != '' and pword != '':
        usr = User.objects.create_user(username=uname ,email=emali, password=pword)
        usr.first_name = fname
        usr.last_name = lname
        usr.save()

        messages.success(request,"Account created successfully!")
        return redirect('/')
    else:
        return redirect('/signup')