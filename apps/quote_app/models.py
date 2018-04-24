# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import users

class quotes_man(models.Manager):
    def quoteValidate(self, postData, user_id):
        user = users.objects.get(id=user_id)

# ----- VALIDATIONS

        errors = []
        response = {
            'status':False,
        }

        name = postData['name']
        quote = postData['quote']

        if len(name) < 3:
        	errors.append("Name should be at least 3 characters long")

        if len(quote) < 10:
        	errors.append("Quote must be at least 10 characters long")

        if not errors:
            response['status'] = True
            newquote = quotes.objects.create(quoted_by=name, quote=quote, uploader=user)
            newquote.favorites.add(user)

        response['errors'] = errors
        return response

class quotes(models.Model):
    quoted_by = models.CharField(max_length=55)
    quote = models.CharField(max_length=455)
    uploader = models.ForeignKey(users, related_name="uploaded_quotes")
    favorites = models.ManyToManyField(users, related_name="favorited_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = quotes_man()
