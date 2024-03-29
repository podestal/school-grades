# Generated by Django 4.2.7 on 2023-12-01 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_grades_api', '0008_alter_assignature_promotion_alter_student_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='school_grades_api.promotion'),
        ),
    ]
