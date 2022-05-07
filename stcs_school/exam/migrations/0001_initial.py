# Generated by Django 4.0.3 on 2022-05-07 20:03

from django.db import migrations, models
import django.db.models.deletion
import exam.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        ('home', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('basicclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basicclass')),
                ('exam_name', models.CharField(choices=[('Monthly Test - 1', 'Monthly Test - 1'), ('Monthly Test - 2', 'Monthly Test - 2'), ('Midterm Exam', 'Midterm Exam'), ('Monthly Test - 3', 'Monthly Test - 3'), ('Monthly Test - 4', 'Monthly Test - 4'), ('Final Exam', 'Final Exam')], max_length=255)),
                ('exam_description', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('batch_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.batch')),
            ],
            options={
                'unique_together': {('batch_year', 'exam_name')},
            },
            bases=('home.basicclass',),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('basicclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basicclass')),
                ('date', models.DateField(validators=[exam.models.Exam.validate_date])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.batchclass')),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.examtype')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.subject')),
            ],
            options={
                'unique_together': {('class_name', 'subject_name', 'exam_type')},
            },
            bases=('home.basicclass',),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('basicclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basicclass')),
                ('marks_assigned', models.PositiveIntegerField()),
                ('marks_gained', models.PositiveIntegerField()),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
                ('examId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
            options={
                'unique_together': {('examId', 'studentId')},
            },
            bases=('home.basicclass',),
        ),
    ]
