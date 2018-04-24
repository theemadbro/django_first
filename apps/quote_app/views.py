# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .forms import *
from django.contrib import messages
from ..loginReg.models import users
from .models import quotes

def quote_home(request):
    print "Logged in user:", request.session['user_id'], ", " + request.session['user']
    currUser = users.objects.get(id=request.session['user_id'])

    form = quoteForm()
    userfavorites = quotes.objects.filter(favorites=currUser)
    quotelist = quotes.objects.exclude(favorites=currUser)

    context = {
        'userfavorites':userfavorites,
        'form':form,
        'quotelist':quotelist
    }
    if request.method == 'POST':
        if 'name' in request.POST:
            response = quotes.objects.quoteValidate(request.POST, request.session['user_id'])
            if response['status']:
                print 'quoteValidate worked'
                return redirect('/quotes')
            else:
                for error in response['errors']:
                    print error
                    messages.error(request, error)
                return redirect('/quotes')
        if 'remove' in request.POST:
            print "remove selected post"
            return redirect('/quotes')


    return render(request, "quote_app/index.html", context)

def user(request, id):
    this = users.objects.get(id=id)
    useruploads = quotes.objects.filter(uploader=this)
    count = useruploads.count()
    context = {

        'user':this,
        'useruploads':useruploads,
        'count':count

    }
    return render(request, "quote_app/showuser.html", context)


def add(request, id):
    this = users.objects.get(id=request.session['user_id'])
    print this.id
    quote = quotes.objects.get(id=id)
    quote.favorites.add(this)
    return redirect('/quotes')

def remove(request, id):
    this = users.objects.get(id=request.session['user_id'])
    quote = quotes.objects.get(id=id)
    quote.favorites.remove(this)
    return redirect('/quotes')