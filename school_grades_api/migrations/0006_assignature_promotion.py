# Generated by Django 4.2.7 on 2023-12-01 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_grades_api', '0005_remove_promotion_assignature'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignature',
            name='promotion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='assgnatures', to='school_grades_api.promotion'),
            preserve_default=False,
        ),
    ]
