# Generated by Django 4.0.3 on 2022-04-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.TextField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('className', models.PositiveIntegerField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=1, null=True)),
                ('kannada', models.PositiveIntegerField(blank=True, null=True)),
                ('english', models.PositiveIntegerField(blank=True, null=True)),
                ('hindi', models.PositiveIntegerField(blank=True, null=True)),
                ('maths', models.PositiveIntegerField(blank=True, null=True)),
                ('science', models.PositiveIntegerField(blank=True, null=True)),
                ('socScience', models.PositiveIntegerField(blank=True, null=True)),
                ('kanGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('engGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('hinGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('matGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('sciGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('socGrade', models.CharField(blank=True, max_length=1, null=True)),
                ('total', models.PositiveIntegerField()),
                ('percentage', models.FloatField()),
                ('grade', models.CharField(blank=True, max_length=1, null=True)),
                ('results', models.TextField(blank=True, max_length=50, null=True)),
                ('passOrFail', models.TextField(blank=True, max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('userid', 'name')},
            },
        ),
    ]