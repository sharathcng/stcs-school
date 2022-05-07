from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser
from account.forms import UserCreateForm, CustomUserChangeForm
from account.models import Staff, Teacher, Student, ParentsDetail

class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    # ordering = ('email',)
    list_display = ('username', 'is_active')
    list_filter = ('is_superuser','role')
    fieldsets = (
        (None, {
            "fields": (
                'username', 'password','role',
            ),
        }),
        ('Permissions', {
            "classes": (),
            "fields": (
                'is_active', 'is_superuser'
            ),
        }),
        ('Important Dates', {
            "classes": ('collapse',),
            "fields": (
                'last_login', 'date_joined'
            ),
        }),
        ('Advanced Options', {
            "classes": ('collapse',),
            "fields": (
                'groups', 'user_permissions'
            ),
        })
    )

    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": (
                'username', 'password1', 'password2', 'is_active', 'is_superuser', 'groups'
            ),
        }),
    )
    # inlines = [
    #     Student_inline,
    #     Teacher_inline,
    # ]



admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(ParentsDetail)