# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"^([a-zA-Z]+[,.]?[ ]?|[a-zA-Z]+['-]?)+$")

import datetime
today = datetime.date.today()

class users_man(models.Manager):
    def userValidate(self, postData):

# ----- VALIDATIONS

        errors = []
        response = {
            'status':False,
        }

# ----- Check for Login
        if 'inemail' in postData:
            print "got login attempt"
            inemail = postData['inemail']
            inpass = postData['inpass']
            listusers = users.objects.filter(email=inemail).all()
            if not listusers:
                print "Username lookup failed"
                errors.append("Username not found.")
        # Checking input password with DB password
            userobj = users.objects.get(email=inemail)
            hash1 = inpass
            if bcrypt.checkpw(hash1.encode(), userobj.password.encode()):
                print "success!"
            else:
                errors.append("Incorrect Password")

            if len(errors) == 0:
                response['status'] = True
                print userobj.username
                response['user'] = userobj
            response['errors'] = errors
            return response
 

# ----- Check for Registration
        if 'name' in postData:
            print "got registration attempt"
            name = postData['name']
            username = postData['username']
            email = postData['email']
            birthday = postData['birthday']
            password = postData['password']
            passcheck = postData['passcheck']
        # Check name input
            if len(name) < 3:
                errors.append("Name must be at least 3 chars long")
            if len(name) > 55:
                errors.append("Name too long!")
            if not NAME_REGEX.match(name):
                errors.append("Name must be a valid name format")
        # Check username input
            if len(username) < 3:
                errors.append("Username must be at least 3 chars long")
            if len(username) > 55:
                errors.append("Username too long!")
        # Check email input
            if len(email) < 4:
                errors.append("Email too short")
            if not EMAIL_REGEX.match(email):
                errors.append("Invalid Email format")
        # Check password inputs
            if len(password) < 8:
                errors.append("Password must be at least 8 charcters long")
            if len(password) > 100:
                errors.append("Password too long for us!")
            if password != passcheck:
                errors.append("Passwords did not match!")
        # Check birthday input
            if birthday > u'today':
                errors.append("Birthday must be before today!")

            if len(errors) == 0:
                hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                userobj = users.objects.create(name=name, username=username, email=email, password=hash1, birthday=birthday)
                response['status'] = True
            response['errors'] = errors
            return response


class users(models.Model):
    name = models.CharField(max_length=35)
    username = models.CharField(max_length=22)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = users_man()

    def __repr__(self):
        return "<user {}: {} {}, {} {} {}>".format(self.id, self.name, self.username, self.email, self.birthday, self.created_at)
