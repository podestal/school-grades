from rest_framework import serializers
from .models import Assignment, Assignature, Professor, Promotion

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id', 'topic', 'description', 'due_date', 'assigment_type', 'assignature']

# class UpdateAssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = ['topic', 'description', 'due_date', 'assigment_type', 'assignature']

class AssignatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignature
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):

    assgnatures = AssignatureSerializer(many=True)
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'assgnatures']