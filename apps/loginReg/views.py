# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect

from django.contrib import messages
from .forms import NameForm
from .models import users
import bcrypt



def index(request):
    if 'user' not in request.session:
        request.session['user'] = ""
        request.session['user_id'] = ""
    print request.session['user_id']
    
    if request.method == 'POST':
    # Processing a Login Request
        if 'inemail' in request.POST:
            response = users.objects.userValidate(request.POST)
            if response['status']:
                request.session['user_id'] = response['user'].id
                request.session['user'] = response['user'].name
                return redirect('/quotes') #--------------------------------------------------------------------------------------
            else:
                for error in response['errors']:
                    messages.error(request, error)
                return redirect('/')
    # Processing a registration Request
        if 'name' in request.POST:
            response = users.objects.userValidate(request.POST)
            if response['status']:
                request.session['user'] = request.POST['name']
                return redirect('/success')
            else:
                for error in response['errors']:
                    messages.error(request, error)
                return redirect('/')
# ----- if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, "loginReg/index.html", {'form': form})

def success(request):
    print "at success"
    return render(request, "loginReg/success.html")

def logout(request):
    request.session['user_id'] = ""
    request.session['user'] = ""
    return redirect('/')