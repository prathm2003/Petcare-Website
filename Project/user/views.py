from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import ContactForm
from .models import ContactMessage

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('confirm-password')

        if password == cpass:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('signup')
            
            my_user = User.objects.create_user(fname, email, password)
            my_user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        pass1 = request.POST.get('password')

        try:
            user = User.objects.get(email=email1)
        except User.DoesNotExist:
            messages.error(request, "No user found with this email")
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=user.username, password=pass1)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('homepage')
        else:
            messages.error(request, "Invalid password")
            return redirect('login')

    return render(request, 'login.html')

def homepage(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def testimonials(request):
    return render(request,'test.html')

def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         user = request.user  # Get the currently logged-in user

    #         # Save contact message to the database
    #         contact_message = ContactMessage(
    #             user=user,
    #             name=name,
    #             email=email,
    #             subject=subject,
    #             message=message
    #         )
    #         contact_message.save()

    #         messages.success(request, 'Your message has been sent successfully!')
    #         return redirect('contact')
    #     else:
    #         messages.error(request, 'There was an error with your form submission.')
    # else:
    #     form = ContactForm()

    return render(request, 'contact.html')
def logout1(request):
    logout(request)
    return redirect('login')


def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Assuming the user is logged in
        user = request.user if request.user.is_authenticated else None

        contact_message = ContactMessage(user=user, name=name, email=email, subject=subject, message=message)
        contact_message.save()

        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    return redirect('contact')