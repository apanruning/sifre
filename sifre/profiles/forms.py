# -*- coding: utf-8 -*-

from django import forms
from profiles.models import DefualtUserProfile


class DefualtUserProfileForm(forms.ModelForm):
    class Meta:
        model = DefualtUserProfile
        exclude = ['user']



