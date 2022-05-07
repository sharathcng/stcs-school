from django.db import models
from django.contrib.auth.models import AbstractUser
from account.managers import CustomUserManager
from home.models import BasicClass

gender_choices = (
    (1, "Male"),
    (2, "Female"),
    (3, "Other")
)

role_choices = (
    (1, "Student"),
    (2, "Teacher"),
    (3, "Staff"),
)

blood_choices = (
    ('O+', "O+"),
    ('O-', "O-"),
    ('A+', "A+"),
    ('A-', "A-"),
    ('B+', "B+"),
    ('B-', "B-"),
    ('AB+', "AB+"),
    ('AB-', "AB-"),
    ('Not Sure', "Not Sure")
)

position_choices = (
    ('1','Accountant'),
    ('2','General Staff'),
)

# Custom User Model

class CustomUser(AbstractUser):
    email = None
    first_name = None
    last_name = None
    role = models.PositiveIntegerField(choices=role_choices, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']
    objects = CustomUserManager()


class Person(BasicClass):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.IntegerField(choices=gender_choices, null=True, blank=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=10, choices=blood_choices,
                                    null=True, blank=True)
    aadhaar_number = models.CharField(max_length=255, blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles', height_field=None,
                                    width_field=None, max_length=None,
                                    blank=True, null=True)
    joining_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

class Teacher(Person):
    user_id = models.OneToOneField(CustomUser,  related_name="currentTeacher", primary_key=True, on_delete=models.CASCADE)
    handling_subjects = models.CharField(max_length=255, blank=True, null=True)
    is_classTeacher = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['user_id']

    def __str__(self):
        return self.full_name

# Staff Model


class Staff(Person):
    user_id = models.OneToOneField(CustomUser,  related_name="currentStaff", primary_key=True, on_delete=models.CASCADE)
    designation = models.PositiveIntegerField(choices=position_choices)

    REQUIRED_FIELDS = ['user_id']

    def __str__(self):
        return self.full_name


class Student(Person):
    user_id = models.OneToOneField(CustomUser,related_name="currentStudent", primary_key=True, on_delete=models.CASCADE)
    started_class = models.CharField(max_length=255, blank=True, null=True)
    current_class = models.ForeignKey("academic.BatchClass", on_delete=models.CASCADE, related_name='current_class')
    is_alumni = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

# parents details Model
class ParentsDetail(BasicClass):
    student_name = models.OneToOneField(Student,related_name="currentParent", primary_key=True, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=50)
    father_qualification = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=255)