from .models import LoginForm
from .forms import LoginForm

from django.shortcuts import render

def login(request):
    username = "not logged in"
   
    if request.method == "POST":
      #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
		
    return render(request, 'loggedin.html', {"username" : username})