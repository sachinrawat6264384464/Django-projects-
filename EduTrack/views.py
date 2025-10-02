from django.shortcuts import render, redirect, get_object_or_404
from .models import UserRegistration, AdminUser
from django.db import IntegrityError
from django.contrib import messages

# -------- User Signup --------


def signup(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            ...
           
            return render(request, 'signup.html', {'success': 'User registered successfully!'})
        return render(request, 'signup.html')
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return render(request, 'signup.html', {'error': f'Unexpected error: {str(e)}'})

# -------- User Login --------
def login(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            user = UserRegistration.objects.get(username=username)
        except UserRegistration.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

        if user.check_password(password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['is_admin'] = False
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# -------- Admin Login --------
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            admin = AdminUser.objects.get(username=username)
        except AdminUser.DoesNotExist:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

        if admin.check_password(password):
            request.session['user_id'] = admin.id
            request.session['username'] = admin.username
            request.session['is_admin'] = True
            return redirect('home')
        else:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

    return render(request, 'admin.html')

# -------- Home Page --------
def index(request):
    context = {
        'username': request.session.get('username'),
        'is_admin': request.session.get('is_admin', False)
    }
    return render(request, 'index.html', context)

# -------- Logout --------
def logout_view(request):
    request.session.flush()
    return redirect('home')

# -------- Student Data (Admin) --------
def studentdata(request):
    students = UserRegistration.objects.all()
    return render(request, 'student_data.html', {'students': students})

# -------- Delete Student --------
def delete_student(request, id):
    student = get_object_or_404(UserRegistration, id=id)
    student.delete()
    return redirect('studentdata')
