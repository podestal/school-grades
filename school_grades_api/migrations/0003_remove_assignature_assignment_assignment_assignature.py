# Generated by Django 4.2.7 on 2023-11-30 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_grades_api', '0002_rename_assigment_assignment_assigment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignature',
            name='assignment',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_grades_api.assignature'),
        ),
    ]
