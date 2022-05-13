from ast import Raise
import math
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from account.forms import UpdateParentForm, UpdateStaffForm, UpdateStudentForm, UpdateTeacherForm, UserCreateForm
from account.models import CustomUser, ParentsDetail, Staff, Student, Teacher
from academic.models import Batch, BatchClass

# Create your views here.


class Dashboard(TemplateView):
    template_name = 'admin-view/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Login(LoginView):
    template_name = "login/login.html"
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        #url = self.get_redirect_url()
        if self.request.user.role == 1:
            messages.success(
                self.request, "Hey, Buddy..! You have been logged in to STCS Student dashboard successfully")
            return reverse_lazy('dashboard')
        elif self.request.user.role == 2:
            messages.success(
                self.request, "Hey, Buddy..! You have been logged in to STCS Teacher dashboard successfully")
            return reverse_lazy('dashboard')
        elif self.request.user.role == 3:
            messages.success(
                self.request, "Hey, Buddy..! You have been logged in to STCS Staff dashboard successfully")
            return reverse_lazy('dashboard')
        else:
            reverse_lazy('login')


class Logout(LogoutView):
    next_page = reverse_lazy('login')

class Teachers(ListView):
    model = Teacher
    template_name = 'admin-view/account/teacher/teachers.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        teachers = Teacher.objects.filter(end_date=None).order_by('full_name')
        return teachers


class Staffs(ListView):
    model = Staff
    template_name = 'admin-view/account/staff/staffs.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffs'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        staffs = Staff.objects.filter(end_date=None)
        return staffs


class CreateTeacher(CreateView):
    model = CustomUser
    template_name = "admin-view/account/teacher/createTeacher.html"
    form_class = UserCreateForm
    initial = {'role': 2}
    success_url = reverse_lazy('teachers')

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_date = request.POST['joinDate'] or None
        handling_subjects = request.POST['subjects'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            newTeacher = Teacher.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                                aadhaar_number=aadhaar_number, handling_subjects=handling_subjects, present_address=present_address, permanent_address=permanent_address, joining_date=started_date)
            messages.success(self.request, "New Teacher created with the name "+str(newTeacher.full_name)+" ..!!!")
            return self.form_valid(form, **kwargs)
        else:
            if aadhaar_number == "":
                messages.error(self.request, "This field cannot be empty")
            elif math.floor(math.log10(int(aadhaar_number)))+1 != 12:
                digit = math.floor(math.log10(int(aadhaar_number)))+1
                messages.error(self.request, "Aadhaar number is always 12 digit, you have entered " +
                               str(digit)+" digit. Please enter correct Aadhaar Number")
            for instance in Teacher.objects.all():
                if instance.aadhaar_number == aadhaar_number:
                    messages.error(self.request, "Aadhaar Number with "+str(aadhaar_number) +
                                   " is already registered with a name - "+instance.full_name+". Please enter the correct Aadhaar Number")
                messages.error(self.request, "Please enter details correctly")
            return render(request, 'admin-view/account/teacher/createTeacher.html', {'form': form})


class CreateStaff(CreateView):
    model = CustomUser
    template_name = "admin-view/account/staff/createStaff.html"
    form_class = UserCreateForm
    initial = {"role": 3}
    success_url = reverse_lazy('staffs')

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_date = request.POST['joinDate'] or None
        designation = request.POST['designation'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            newStaff = Staff.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                            aadhaar_number=aadhaar_number, present_address=present_address, permanent_address=permanent_address, joining_date=started_date, designation=designation)
            messages.success(self.request, "New Staff created with the name "
                             + str(newStaff.full_name)+"..!!!")
            return self.form_valid(form, **kwargs)
        else:
            if aadhaar_number == "":
                messages.error(self.request, "This field cannot be empty")
            elif math.floor(math.log10(int(aadhaar_number)))+1 != 12:
                digit = math.floor(math.log10(int(aadhaar_number)))+1
                messages.error(self.request, "Aadhaar number is always 12 digit, you have entered " +
                               str(digit)+" digit. Please enter correct Aadhaar Number")
            for instance in Staff.objects.all():
                if instance.aadhaar_number == aadhaar_number:
                    messages.error(self.request, "Aadhaar Number with "+str(aadhaar_number) +
                                   " is already registered with a name - "+instance.full_name+". Please enter the correct Aadhaar Number")
            messages.error(self.request, "Please enter details correctly")
            return render(request, 'admin-view/account/staff/createStaff.html', {'form': form})


class DisableTeacher(RedirectView):
    pattern_name = 'teachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableTeacher(RedirectView):
    pattern_name = 'teachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)


class DisableStudent(RedirectView):
    pattern_name = 'students'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args, kwargs['clsObj'])


class EnableStudent(RedirectView):
    pattern_name = 'students'

    def get_redirect_url(self, *args, **kwargs):
        userObj = CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args, kwargs['clsObj'])


class DisableStaff(RedirectView):
    pattern_name = 'staffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableStaff(RedirectView):
    pattern_name = 'staffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)


class UpdateTeacherProfile(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'admin-view/account/teacher/editProfile.html'
    success_url = reverse_lazy('teachers')
    context_object_name = 'teacherObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        teacherObj = Teacher.objects.get(user_id=userObj)
        return teacherObj


class UpdateStaffProfile(UpdateView):
    model = Staff
    form_class = UpdateStaffForm
    template_name = 'admin-view/account/staff/editProfile.html'
    success_url = reverse_lazy('staffs')
    context_object_name = 'staffObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        staffObj = Staff.objects.get(user_id=userObj)
        return staffObj


class ViewTeacherProfile(TemplateView):
    template_name = 'admin-view/account/teacher/viewProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        context['teacherObj'] = get_object_or_404(Teacher, user_id=user_id)
        return context


class ViewStaffProfile(TemplateView):
    template_name = 'admin-view/account/staff/viewProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        context['staffObj'] = get_object_or_404(Staff, user_id=user_id)
        return context


class Students(ListView):
    model = Student
    template_name = 'admin-view/account/student/students.html'
    paginate_by = 8
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = BatchClass.objects.get(id=self.kwargs['pk'])
        context['className'] = className
        context['students'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        className = BatchClass.objects.get(id=self.kwargs['pk'])
        students = Student.objects.filter(current_class=className)
        return students


class ViewStudentProfile(TemplateView):
    template_name = 'admin-view/account/student/viewProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        studentData = Student.objects.get(user_id=user_id)
        parentData = ParentsDetail.objects.get(student_name=studentData)
        context['studObj'] = studentData
        context['parentObj'] = parentData
        return context


class UpdateStudentProfile(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    template_name = 'admin-view/account/student/editProfile.html'
    context_object_name = 'studObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        studObj = Student.objects.get(user_id=userObj)
        return studObj

    def get_success_url(self):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        studObj = Student.objects.get(user_id=userObj)
        return reverse_lazy('allClasses')


class CreateStudent(CreateView):
    model = CustomUser
    template_name = "admin-view/account/student/createStudent.html"
    form_class = UserCreateForm
    initial = {"role": 1}
    success_url = reverse_lazy('allClasses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classList'] = BatchClass.objects.filter(
            batch_year=Batch.objects.last())
        return context

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth'] or None
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_class = request.POST['startedClass'] or None
        current_class = BatchClass.objects.get(id=request.POST['currentClass'])
        joining_date = request.POST['joinDate'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            newStudent = Student.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                                aadhaar_number=aadhaar_number, present_address=present_address, permanent_address=permanent_address, started_class=started_class, current_class=current_class, joining_date=joining_date)
            messages.success(self.request, "New student created with the name "+ str(fullName)+" for the class "+str(current_class)+" ..!!!")
            ParentsDetail.objects.create(student_name = newStudent)
            return self.form_valid(form, **kwargs)
        else:
            classList = BatchClass.objects.filter(batch_year=Batch.objects.last())
            messages.error(self.request, "Please enter right details")
            return render(request, 'admin-view/account/student/createStudent.html', {'form': form, 'classList': classList})

class UpdateTeacherMyProfile(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'admin-view/account/teacher/editProfile.html'
    context_object_name = 'teacherObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.request.user.username)
        teacherObj = Teacher.objects.get(user_id=userObj)
        return teacherObj
    def get_success_url(self):
        messages.success(self.request,"Your profile details has been updated.")
        return reverse_lazy('dashboard')

class UpdateStaffMyProfile(UpdateView):
    model = Staff
    form_class = UpdateStaffForm
    template_name = 'admin-view/account/staff/editProfile.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'staffObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.request.user.username)
        staffObj = Staff.objects.get(user_id=userObj)
        return staffObj
    def get_success_url(self):
        messages.success(self.request,"Your profile details has been updated.")
        return reverse_lazy('dashboard')
        
class UpdateStudentMyProfile(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    template_name = 'admin-view/account/student/editProfile.html'
    context_object_name = 'studObj'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.request.user.username)
        studObj = Student.objects.get(user_id=userObj)
        return studObj
    def get_success_url(self):
        messages.success(self.request,"Your profile details has been updated.")
        return reverse_lazy('dashboard')


class UpdateParentDetails(UpdateView):
    model = ParentsDetail
    form_class = UpdateParentForm
    template_name = 'admin-view/account/student/editParentDetails.html'
    context_object_name = 'parentObj'

    def get_object(self, queryset=None):
        print(self.kwargs['pk'])
        studentObj = Student.objects.get(full_name=self.kwargs['pk'])
        parentObj = ParentsDetail.objects.get(student_name=studentObj)
        return parentObj

    def get_success_url(self):
        studentObj = Student.objects.get(full_name=self.kwargs['pk'])
        return reverse_lazy('view-student-profile',kwargs={'pk':studentObj.user_id})