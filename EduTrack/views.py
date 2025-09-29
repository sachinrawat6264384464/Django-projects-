from django.shortcuts import render, redirect
from .models import UserRegistration,AdminUser
from django.db import IntegrityError

from django.contrib.auth import authenticate, login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if UserRegistration.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})

        try:
            user = UserRegistration(
                name=name,
                mobile=mobile,
                address=address,
                username=username
            )
            user.set_password(password)  # 🔑 Hash password before saving
            user.save()
            return render(request, 'signup.html', {'success': 'User registered successfully!'})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'DB error, try again'})

    return render(request, 'signup.html')





def login(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            user = UserRegistration.objects.get(username=username)
        except UserRegistration.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

        if user.check_password(password):
            # set manual session
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')  # index page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import AdminUser

def admin(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            user = AdminUser.objects.get(username=username)
        except AdminUser.DoesNotExist:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

        if user.check_password(password):
            # set manual session
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['is_admin'] = True  # 👈 ye flag add karo
            return redirect('home')
        else:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

    return render(request, 'admin.html')

def index(request):
    context = {
        'username': request.session.get('username'),
        'is_admin': request.session.get('is_admin', False)  # default False
    }
    return render(request, 'index.html', context)


def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('home')
    
def studentdata(request):
    return render(request, 'student_data.html')
    
