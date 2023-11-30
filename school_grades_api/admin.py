from django.contrib import admin
from school_grades_api import models

admin.site.register(models.Assignature)
admin.site.register(models.Assignment)
admin.site.register(models.Professor)
admin.site.register(models.Promotion)
admin.site.register(models.Student)
admin.site.register(models.Tutor)