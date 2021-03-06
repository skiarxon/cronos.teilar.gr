# -*- coding: utf-8 -*-

from django import forms

class EclassCredentialsForm(forms.Form):
    eclass_username = forms.CharField(max_length = 30)
    eclass_password = forms.CharField(max_length = 30, widget = forms.PasswordInput())

class WebmailForm(forms.Form):
    webmail_username = forms.CharField(max_length = 30)
    webmail_password = forms.CharField(max_length = 30, widget = forms.PasswordInput())

class DeclarationForm(forms.Form):
    declaration = forms.CharField(widget = forms.HiddenInput())

class GradesForm(forms.Form):
    grades = forms.CharField(widget = forms.HiddenInput())

class EclassLessonsForm(forms.Form):
    eclass_lessons = forms.CharField(widget = forms.HiddenInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, label = 'Όνομα Χρήστη:')
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput(), label = 'Κωδικός Πρόσβασης:')
    remember = forms.BooleanField(required = False, label = 'Να με θυμάσαι')
