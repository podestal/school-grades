from rest_framework import serializers
from .models import Assignment, Assignature, Professor, Promotion, Student

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id', 'topic', 'description', 'due_date', 'assigment_type', 'assignature', 'student']

# class UpdateAssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = ['topic', 'description', 'due_date', 'assigment_type', 'assignature']

class AssignatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignature
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):

    assignatures = AssignatureSerializer(many=True)
    class Meta:
        model = Professor
        fields = ['id', 'assignatures']

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):

    assignatures = AssignatureSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Promotion
        fields = ['id', 'name', 'assignatures', 'students']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'