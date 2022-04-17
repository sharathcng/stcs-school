from operator import truediv
from pyexpat import model
from django.db import models

# Create your models here.
class Result(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.TextField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    className = models.PositiveIntegerField(null=True, blank=True)
    section = models.CharField(max_length=1, null=True, blank=True)
    kannada = models.PositiveIntegerField(null = True, blank = True)
    english = models.PositiveIntegerField(null = True, blank = True)
    hindi = models.PositiveIntegerField(null = True, blank = True)
    maths = models.PositiveIntegerField(null = True, blank = True)
    science = models.PositiveIntegerField(null = True, blank = True)
    socScience = models.PositiveIntegerField(null = True, blank = True)
    kanGrade = models.CharField(max_length=1, null = True, blank = True)
    engGrade = models.CharField(max_length=1, null = True, blank = True)
    hinGrade = models.CharField(max_length=1, null = True, blank = True)
    matGrade = models.CharField(max_length=1, null = True, blank = True)
    sciGrade = models.CharField(max_length=1, null = True, blank = True)
    socGrade = models.CharField(max_length=1, null = True, blank = True)
    total = models.PositiveIntegerField(null = True, blank = True)
    percentage = models.FloatField(null = True, blank = True)
    grade = models.CharField(max_length=1, null = True, blank = True)
    results = models.TextField(max_length=50, null = True, blank = True)
    passOrFail = models.TextField(max_length=4, null=True, blank=True)
    feesPaid = models.BooleanField()

    class Meta:
        unique_together = ('userid','name')