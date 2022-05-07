from faulthandler import disable
from django import forms
from django.forms.widgets import DateInput, TextInput
from account.models import Teacher
from .models import Batch, BatchClass, Subject, TeacherAllocation
from django.core.exceptions import NON_FIELD_ERRORS


class BatchCreateForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            'batch_year',
            'start_date',
            'end_date',
        ]

        widgets = {
            'batch_year': forms.TextInput(attrs={'placeholder': 'Enter Batch Year', 'class': 'form-control', 'type': 'text', 'aria-describedby': 'floatingInputHelp'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = BatchClass
        fields = [
            'batch_year',
            'class_name',
            'class_section',
            'class_teacher',
        ]

        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control', 'hidden': 'hidden'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the class number'}),
            'class_section': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the section name'}),
            'class_teacher': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Enter the class number'}),

        }

    def __init__(self, *args, **kwargs):
        super(ClassCreateForm, self).__init__(*args, **kwargs)
        self.fields['class_teacher'].queryset = Teacher.objects.filter(end_date=None)
        self.fields['batch_year'].initial = Batch.objects.last()


class UpdateClassForm(forms.ModelForm):
    class Meta:
        model = BatchClass
        fields = '__all__'
        widgets = {
            'batch_year': forms.Select(attrs={'class': 'form-select'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_section': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-select'}),
        }


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'subject_name',
        ]

        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject name'}),
        }


class UpdateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject name'}),
        }


class TeacherAllocateCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherAllocation
        fields = [
            'batch_year',
            'class_name',
            'subject_name',
            'teacher_name',
        ]

        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control','hidden':'hidden'}),
            'class_name': forms.Select(attrs={'class': 'form-select'}),
            'subject_name': forms.Select(attrs={'class': 'form-select'}),
            'teacher_name': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherAllocateCreateForm, self).__init__(*args, **kwargs)
        self.fields['class_name'].queryset = BatchClass.objects.filter(batch_year=Batch.objects.last())
        self.fields['batch_year'].initial = Batch.objects.last()

class TeacherAllocateUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherAllocation
        fields = [
            'batch_year',
            'class_name',
            'subject_name',
            'teacher_name',
        ]

        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control','hidden':'hidden'}),
            'class_name': forms.Select(attrs={'class': 'form-select'}),
            'subject_name': forms.Select(attrs={'class': 'form-select'}),
            'teacher_name': forms.Select(attrs={'class': 'form-select'}),
        }