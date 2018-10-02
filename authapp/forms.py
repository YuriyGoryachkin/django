# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
# from .models import UserMessenger
#
#
# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = UserMessenger
#         fields = ('username', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#
# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = UserMessenger
#         fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')
#
#         def __init__(self, *args, **kwargs):
#             super(UserRegisterForm, self).__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.widget.attrs['class'] = 'form-control'
#                 field.help_text = ''
#
#         def clean_age(self):
#             data = self.cleaned_data['age']
#             if data < 18:
#                 raise forms.ValidationError('Вы слишком молоды')
#
#             return data
#
#
# class UserEditForm(UserChangeForm):
#     class Meta:
#         model = UserMessenger
#         fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')
#
#         def __init__(self, *args, **kwargs):
#             super(UserEditForm, self).__init__(*args, **kwargs)
#             for field_name, filed in self.fields.items():
#                 filed.widget.attrs['class'] = 'form-control'
#                 filed.help_text = ''
#
#                 if field_name == 'password':
#                     filed.widget = forms.HiddenInput()
#
#         def clean_age(self):
#             data =self.cleaned_data['age']
#             if data < 18:
#                 raise forms.ValidationError('Вы слишком молоды')
#
#             return data
