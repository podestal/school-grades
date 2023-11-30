from django.db import models
from django.conf import settings

class Assignment(models.Model):

    ASSIGNMENT_HOMEWORK = 'h'
    ASSIGNMENT_PROJECT = 'p'
    ASSIGNMENT_QUIZZ = 'q'
    ASSIGNMENT_TEST = 't'

    ASSIGNMENT_CHOICES = [
        (ASSIGNMENT_HOMEWORK, 'Homework'),
        (ASSIGNMENT_PROJECT, 'Project'),
        (ASSIGNMENT_QUIZZ, 'Quizz'),
        (ASSIGNMENT_TEST, 'Test'),
    ]

    topic = models.CharField(max_length=255)
    description = models.TextField()
    presented = models.BooleanField()
    grade = models.DecimalField(decimal_places=1, max_digits=3)
    due_date = models.DateTimeField()
    assigment = models.CharField(max_length=1, choices=ASSIGNMENT_CHOICES)

class Assignature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    assignature = models.ForeignKey(Assignature, on_delete=models.PROTECT)

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)

class Professor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignature = models.ForeignKey(Assignature, on_delete=models.PROTECT)

class Tutor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)



