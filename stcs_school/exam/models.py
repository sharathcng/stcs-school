from django.db import models
from django.db.models.fields import AutoField
from django.core.exceptions import ValidationError
from django.utils import timezone

from home.models import BasicClass

exam_choices = (
    ('Monthly Test - 1',"Monthly Test - 1"),
    ("Monthly Test - 2","Monthly Test - 2"),
    ("Midterm Exam","Midterm Exam"),
    ("Monthly Test - 3","Monthly Test - 3"),
    ("Monthly Test - 4","Monthly Test - 4"),
    ("Final Exam","Final Exam"),
)

# Assessment_type Model
class ExamType(BasicClass):
    batch_year = models.ForeignKey("academic.Batch",on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=255, choices = exam_choices)
    exam_description = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = (('batch_year','exam_name'),)

    def __str__(self):
        return self.assessment_name

class Exam(BasicClass):
    def validate_date(date):
        if date < timezone.now().date():
            raise ValidationError("Please select date from today onwards.")

    exam_type = models.ForeignKey("exam.ExamType",on_delete=models.CASCADE)
    class_name = models.ForeignKey("academic.BatchClass",on_delete=models.CASCADE)
    subject_name = models.ForeignKey("academic.Subject",on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, validators=[validate_date])
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = ('class_name','subject_name','exam_type',)

    def __str__(self):
        return str(self.class_name)+' - '+str(self.subject)+' - '+str(self.assessment_type)

class Result(BasicClass):
    examId = models.ForeignKey("exam.Exam",on_delete=models.CASCADE)
    studentId = models.ForeignKey("account.Student",on_delete=models.CASCADE)
    marks_assigned = models.PositiveIntegerField()
    marks_gained = models.PositiveIntegerField()
    grade = models.CharField(max_length=5, null = True, blank = True)

    class Meta:
        unique_together = ('examId','studentId',)