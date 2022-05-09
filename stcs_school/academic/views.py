from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from account.models import Student
from .forms import BatchCreateForm, ClassCreateForm, TeacherAllocateCreateForm, TeacherAllocateUpdateForm, TimeTableUploadForm, UpdateClassForm, SubjectCreateForm, UpdateSubjectForm
from .models import Attendance, Batch, BatchClass, Subject, TeacherAllocation, TimeTable
from django.contrib import messages
from django.urls.base import reverse_lazy
from datetime import datetime, date
from django.db import transaction
from django.views.generic.edit import FormView

# Displaying all batches in a list
class Batches(ListView):
    model = Batch
    template_name = "admin-view/academic/batches.html"
    context_object_name = 'batchItems'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        batchItems = Batch.objects.all().order_by('-batch_year')
        return batchItems

# Creating new batch


class CreateBatch(CreateView):
    model = Batch
    template_name = "admin-view/academic/createForms/batchCreateForm.html"
    form_class = BatchCreateForm
    success_url = reverse_lazy('batch')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "You have created a new batch for this year..!!!")
        return super().form_valid(form)


# Batchwise classes list
class BatchClasses(ListView):
    model = Batch
    template_name = "admin-view/academic/classes.html"
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        studentCount = []
        batchItem = Batch.objects.get(batch_year=self.kwargs['pk'])
        batchClasses = BatchClass.objects.filter(batch_year=batchItem)
        for each in batchClasses:
            studentCount.append(Student.objects.filter(
                current_class=each.id).count())
        classes = list(zip(batchClasses, studentCount))
        return classes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batchItem = Batch.objects.get(batch_year=self.kwargs['pk'])
        context['classes'] = self.get_queryset()
        if batchItem:
            context['batchName'] = batchItem.batch_year
        else:
            None
        return context


# Present year classes list
class AllClasses(ListView):
    model = BatchClass
    template_name = "admin-view/academic/classes.html"
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        studentCount = []
        batchItem = Batch.objects.last()
        batchClasses = BatchClass.objects.filter(batch_year=batchItem)
        for each in batchClasses:
            studentCount.append(Student.objects.filter(
                current_class=each.id).count())
        classes = list(zip(batchClasses, studentCount))
        return classes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batchItem = Batch.objects.last()
        context['classes'] = self.get_queryset()
        if batchItem:
            context['batchName'] = batchItem.batch_year
        else:
            None
        return context


class CreateClass(CreateView):
    model = BatchClass
    template_name = "admin-view/academic/createForms/classCreateForm.html"
    form_class = ClassCreateForm

    def get_success_url(self):
        return reverse_lazy('allClasses')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "You have created a new class with the name " +
                         "\""+self.object.class_name+" " + self.object.class_section+"\"..!!!")
        return super().form_valid(form)


class UpdateClassDetails(UpdateView):
    model = BatchClass
    template_name = 'admin-view/academic/editForms/classEditForm.html'
    form_class = UpdateClassForm
    success_url = reverse_lazy('allClasses')
    context_object_name = 'classItem'

    def get_object(self, queryset=None):
        classItem = BatchClass.objects.get(id=self.kwargs['pk'])
        return classItem


class Subjects(ListView):
    model = Subject
    template_name = "admin-view/academic/subjects.html"


class CreateSubject(CreateView):
    model = Subject
    template_name = "admin-view/academic/createForms/subjectCreateForm.html"

    form_class = SubjectCreateForm
    success_url = reverse_lazy('subjects')


class UpdateSubject(UpdateView):
    model = Subject
    form_class = UpdateSubjectForm
    template_name = 'admin-view/academic/editForms/subjectEditForm.html'
    success_url = reverse_lazy('subjects')
    context_object_name = 'subjectObj'

    def get_object(self, queryset=None):
        subjectObj = Subject.objects.get(id=self.kwargs['pk'])
        return subjectObj


class DeleteSubject(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')


class CreateTeacherAllocation(CreateView):
    model = TeacherAllocation
    template_name = "admin-view/academic/createForms/createAllocation.html"
    form_class = TeacherAllocateCreateForm
    success_url = reverse_lazy('teacher-allocation')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "You have allocated \""+str(self.object.teacher_name)+"\"" +
                         " for teaching \""+str(self.object.subject_name)+"\" for the class "+str(self.object.class_name)+"..!!!")
        return super().form_valid(form)


class AllocateTeacher(ListView):
    model = TeacherAllocation
    template_name = "admin-view/academic/allocationList.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batchName = Batch.objects.last()
        context['teacherAlloc'] = self.get_queryset()
        if batchName:
            context['batchName'] = batchName.batch_year
        else:
            None
        return context

    def get_queryset(self, *args, **kwargs):
        teacherAlloc = TeacherAllocation.objects.filter(
            batch_year=Batch.objects.last())
        return teacherAlloc


class UpdateTeacherAllocation(UpdateView):
    model = TeacherAllocation
    form_class = TeacherAllocateUpdateForm
    template_name = 'admin-view/academic/editForms/teachAllocEditForm.html'
    success_url = reverse_lazy('teacher-allocation')
    context_object_name = 'teacherAlloc'

    def get_object(self, queryset=None):
        teacherAlloc = TeacherAllocation.objects.get(id=self.kwargs['pk'])
        return teacherAlloc


class DeleteTeacherAllocation(DeleteView):
    model = TeacherAllocation
    success_url = reverse_lazy('teacher-allocation')


# Present year classes list
class AttendanceClasses(ListView):
    model = BatchClass
    template_name = "admin-view/attendance/classes.html"
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        studentCount = []
        batchItem = Batch.objects.last()
        batchClasses = BatchClass.objects.filter(batch_year=batchItem)
        for each in batchClasses:
            studentCount.append(Student.objects.filter(
                current_class=each.id).count())
        classes = list(zip(batchClasses, studentCount))
        return classes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batchItem = Batch.objects.last()
        context['classes'] = self.get_queryset()
        if batchItem:
            context['batchName'] = batchItem.batch_year
        else:
            None
        return context


class AttendanceDates(ListView):
    model = Attendance
    template_name = "admin-view/attendance/attendancePage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = BatchClass.objects.get(id=self.kwargs['pk'])
        attendance = Attendance.objects.filter(class_name=className).values('date').distinct()
        attendanceCount = attendance.count()
        context['attendance'] = attendance
        context['className'] = className
        context['attendanceCount'] = attendanceCount
        return context


class ViewAttendance(ListView):
    model = Attendance
    template_name = "admin-view/attendance/viewAttendance.html"

    def get_context_data(self, **kwargs):
        attendanceCountList = []
        studentList = []
        context = super().get_context_data(**kwargs)
        className = BatchClass.objects.get(id=self.kwargs['pk1'])
        attendanceList = Attendance.objects.filter(class_name=className).values('student_name').distinct()
        for stud in attendanceList:
            attendanceCountList.append(Attendance.objects.filter(student_name=stud['student_name'],morng_presence = True).values('date').distinct().count())
            studentList.append(Student.objects.get(user_id=stud['student_name']))
        attendanceCount = Attendance.objects.filter(class_name=className).values('date').distinct().count()
        context['className'] = className
        context['attendanceCount'] = attendanceCount
        attendance = list(zip(studentList, attendanceCountList))
        context['attendance'] = attendance
        return context


class TakeAttendance(ListView):
    model = Attendance
    template_name = "admin-view/attendance/students.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = BatchClass.objects.get(id=self.kwargs['pk'])
        students = Student.objects.filter(current_class=className)
        with transaction.atomic():
            for stud in students:
                Attendance.objects.update_or_create(class_name=className, date=date.today(), student_name=stud)
        attendance = Attendance.objects.filter(class_name=className, date=date.today())
        attendanceCount = Attendance.objects.filter(class_name=className).values('date').distinct().count()
        context['attendance'] = attendance
        context['className'] = className
        context['attendanceCount'] = attendanceCount
        return context


def UpdateOldAttendance(request, pk):
    if request.method == 'POST':
        className = BatchClass.objects.get(id=pk)
        students = Student.objects.filter(current_class=className)
        oldDate = request.POST['oldDate']
        with transaction.atomic():
            for stud in students:
                Attendance.objects.update_or_create(class_name=className, date=oldDate, student_name=stud)
        attendance = Attendance.objects.filter(class_name=className, date=oldDate)
        attendanceCount = Attendance.objects.filter(class_name=className).values('date').distinct().count()
        return render(request,'admin-view/attendance/students.html', {'className': className, 'attendance':attendance, 'attendanceCount':attendanceCount})
    else:
        className = BatchClass.objects.get(id=pk)
        attendanceCount = Attendance.objects.filter(class_name=className).values('date').distinct().count()
        return render(request,'admin-view/attendance/oldAttendance.html', {'className': className,'attendanceCount':attendanceCount})


class SaveAttendance(FormView):
    def post(self, request, *args, **kwargs):
        classID = request.POST['className']
        className = BatchClass.objects.get(id = classID)
        attendance = Attendance.objects.filter(class_name=className).values('date').distinct()
        attendanceCount = attendance.count()
        sid = request.POST.getlist('sid')
        morning = request.POST.getlist('morning')
        afternoon = request.POST.getlist('afternoon')
        with transaction.atomic():
            for each in sid:
                if each in morning:
                    Attendance.objects.filter(id=each).update(morng_presence=True)
                else:
                    Attendance.objects.filter(id=each).update(morng_presence=False)
                if each in afternoon:
                    Attendance.objects.filter(id=each).update(aftrn_presence=True)
                else:
                    Attendance.objects.filter(id=each).update(aftrn_presence=False)
        return render(request,'admin-view/attendance/attendancePage.html', {'className': className, 'attendance':attendance, 'attendanceCount':attendanceCount})


class UploadTimeTable(CreateView):
    model = TimeTable
    form_class = TimeTableUploadForm
    template_name = 'admin-view/timeTable/uploadPage.html'

    def get_success_url(self):
        messages.success(self.request,"Timetable uploaded successfully")
        return reverse_lazy('view-time-table')

class ViewTimeTable(ListView):
    model = TimeTable
    template_name = 'admin-view/timeTable/viewPage.html'
    context_object_name = 'timeTables'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        timeTables = TimeTable.objects.all().order_by('class_name')
        return timeTables

class UpdateTimeTable(UpdateView):
    model = TimeTable
    form_class = TimeTableUploadForm
    template_name = 'admin-view/timeTable/uploadPage.html'

    def get_object(self, queryset=None):
        teacherAlloc = TimeTable.objects.get(id=self.kwargs['pk'])
        return teacherAlloc

    def get_success_url(self):
        messages.success(self.request,"Timetable uploaded successfully")
        return reverse_lazy('view-time-table')