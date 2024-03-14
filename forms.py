# voting/forms.py

from django import forms
from .models import Target
from .models import Group

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'group']  # 投票対象の名前とグループを収集するフィールド

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
