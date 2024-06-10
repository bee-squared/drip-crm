from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
  # Check to see if logging in
  if request.method == 'POST':
    print(request)
    username = request.POST['username'] # matches the form field name username
    password = request.POST['password'] # matches the form field name password

    #Authenticate
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, "You have been logged in!")
      return redirect('home')
    else:
      messages.error(request, "There was an error logging in, please try again.")
      return redirect('home')
  else:
    return render(request, 'home.html', {})

def logout_user(request):
  logout(request)
  messages.success(request, "You have been logged out")
  return redirect('home')

