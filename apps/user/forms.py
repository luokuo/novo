from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)  # username字段验证
    password = forms.CharField(required=True)  # password字段验证

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
