# Generated by Django 4.0.3 on 2022-04-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_remove_result_created_at_remove_result_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
