# Generated by Django 4.0.3 on 2022-05-07 20:03

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        ('home', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveIntegerField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Staff')], null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('basicclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basicclass')),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('Not Sure', 'Not Sure')], max_length=10, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=255, null=True)),
                ('present_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            bases=('home.basicclass',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='account.person')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='currentStaff', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.PositiveIntegerField(choices=[('1', 'Accountant'), ('2', 'General Staff')])),
            ],
            bases=('account.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='account.person')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='currentStudent', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('started_class', models.CharField(blank=True, max_length=255, null=True)),
                ('is_alumni', models.BooleanField(default=False)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_class', to='academic.batchclass')),
            ],
            bases=('account.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='account.person')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='currentTeacher', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('handling_subjects', models.CharField(blank=True, max_length=255, null=True)),
                ('is_classTeacher', models.BooleanField(default=False)),
            ],
            bases=('account.person',),
        ),
        migrations.CreateModel(
            name='ParentsDetail',
            fields=[
                ('basicclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='home.basicclass')),
                ('student_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='currentParent', serialize=False, to='account.student')),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('father_occupation', models.CharField(max_length=255)),
                ('mother_occupation', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=50)),
                ('father_qualification', models.CharField(max_length=255)),
                ('mother_qualification', models.CharField(max_length=255)),
            ],
            bases=('home.basicclass',),
        ),
    ]
