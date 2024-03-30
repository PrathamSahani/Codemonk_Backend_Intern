from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *


# Define a view function for the login page
def login_page(request):
    
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
     
    # Render the login page template (GET request)
    return render(request, 'login.html')
 
# Define a view function for the registration page
def register_page(request):
    
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/login/')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')


def custom_logout(request):
    logout(request)
    return redirect('/login/') 

@login_required(login_url='/login/')
def paragraphs(request):
    if request.method == 'POST':
        data = request.POST
        paragraph_name = data.get('paragraph_name')
        paragraph_description = data.get('paragraph_description')

        Paragraph.objects.create(
            paragraph_name=paragraph_name,
            paragraph_description=paragraph_description,
        )
        return redirect('/')

    queryset = Paragraph.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            Q(paragraph_name__icontains=request.GET.get('search')) & Q(paragraph_description__icontains=request.GET.get('search'))
        )
   

    context = {'paragraphs': queryset}
    return render(request, 'paragraphs.html', context)


def delete_paragraph(request, id):
    queryset = Paragraph.objects.get(id=id)
    queryset.delete()
    return redirect('home')


@login_required(login_url='/login/')
def update_paragraph(request, id):
    queryset = Paragraph.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        
        paragraph_name = data.get('paragraph_name')
        paragraph_description = data.get('paragraph_description')

        queryset.paragraph_name = paragraph_name
        queryset.paragraph_description = paragraph_description

        queryset.save()
        return redirect('/')

    context = {'paragraph': queryset}
    return render(request, 'update_paragraph.html', context)

def home(request):
    if request.method == 'POST':
        data = request.POST
        paragraph_name = data.get('paragraph_name')
        paragraph_description = data.get('paragraph_description')

        Paragraph.objects.create(
            paragraph_name=paragraph_name,
            paragraph_description=paragraph_description,
        )
        return redirect('/')
    queryset = Paragraph.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(
            Q(paragraph_name__icontains=request.GET.get('search')) | Q(paragraph_description__icontains=request.GET.get('search'))
        )

    context = {'paragraphs': queryset}
    return render(request, 'home.html', context)
