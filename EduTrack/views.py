from django.shortcuts import render, redirect
from .models import UserRegistration

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Optional: password confirm check
        if password != confirm_password:
            return render(request, 'index.html', {'error': 'Passwords do not match'})

        # Save to DB
        UserRegistration.objects.create(
            name=name,
            mobile=mobile,
            address=address,
            username=username,
            password=password,
            confirm_password=confirm_password
        )
        return render(request, 'index.html', {'success': 'User registered successfully!'})

    return render(request, 'index.html')
