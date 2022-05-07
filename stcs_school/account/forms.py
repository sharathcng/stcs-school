from dataclasses import field
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from account.models import CustomUser, ParentsDetail, Staff, Student, Teacher
from django import forms
from django import forms
import math


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'role',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter unique name'}),
            'role': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password2'].widget.attrs["class"] = "form-control"
        self.fields['password1'].widget.attrs["placeholder"] = "Enter strong password"
        self.fields['password2'].widget.attrs["placeholder"] = "Enter above password"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'role',
        ]


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['user_id']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'aadhaar_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateTeacherForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False


class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user_id']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'aadhaar_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateStaffForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user_id']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'aadhaar_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'started_class': forms.TextInput(attrs={'class':'form-control'}),
            'current_class': forms.Select(attrs={'class':'form-select'})

        }

    def __init__(self, *args, **kwargs):
        super(UpdateStudentForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False

class UpdateParentForm(forms.ModelForm):
    class Meta:
        model = ParentsDetail
        exclude = ['student_name']
        widgets = {
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control'}),
            'father_qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_qualification': forms.TextInput(attrs={'class': 'form-control'}),
        }