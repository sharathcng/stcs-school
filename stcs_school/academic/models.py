from django.db import models

from home.models import BasicClass
from account.models import Student

#Session Year Model
class Batch(models.Model):
    batch_year = models.CharField(max_length=50,primary_key=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.batch_year
    
    unique_together = (['batch_year'])


class BatchClass(BasicClass):
    batch_year = models.ForeignKey("academic.Batch",on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    class_section = models.CharField(max_length=255)
    class_teacher = models.ForeignKey("account.Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name+self.class_section
        
    class Meta:
        unique_together = (['batch_year','class_name','class_section','class_teacher'])


class Subject(BasicClass):
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subject_name
    class Meta:
        unique_together = (['subject_name'])


class TeacherAllocation(BasicClass):
    batch_year = models.ForeignKey("Batch",on_delete=models.CASCADE)
    class_name = models.ForeignKey("BatchClass",on_delete=models.CASCADE)
    subject_name = models.ForeignKey("Subject",on_delete=models.CASCADE)
    teacher_name = models.ForeignKey("account.Teacher",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.class_name)+'-'+str(self.subject_name)+'-'+str(self.teacher_name)

    class Meta:
        unique_together = ('batch_year','class_name','subject_name',)

class Attendance(BasicClass):
    class_name  = models.ForeignKey(BatchClass, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    morng_presence = models.BooleanField(default=True)
    aftrn_presence = models.BooleanField(default=True)