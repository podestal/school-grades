# Generated by Django 4.2.7 on 2023-12-01 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_grades_api', '0004_alter_assignment_grade_alter_assignment_presented'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='assignature',
        ),
    ]