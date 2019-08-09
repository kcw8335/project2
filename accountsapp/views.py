from django.shortcuts import render, redirect
from accountsapp.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            user = User.objects.get(email=request.POST['mb_id'])
            return render(request, 'signup.html', {'error': '이미 사용중인 아이디입니다.'})
        except User.DoesNotExist:
            #self.model(email=email, username=username,registered=adress, phone=phone_number, **extra_fields)
            user = User.objects.create_user(
                email=request.POST['mb_id'], 
                username=request.POST['mb_name'], 
                password=request.POST['mb_pass'],
                registered=request.POST['addr1'],
                phone=request.POST['mb_tel21']+request.POST['mb_tel22']+request.POST['mb_tel23'],
                )
            auth.login(request, user)
            return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error': 'email or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'signup.html')
