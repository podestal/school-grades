from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Assignment, Assignature, Professor, Promotion, Student
from .serializers import AssignmentSerializer, AssignatureSerializer, ProfessorSerializer, PromotionSerializer, CreatePromotionSerializer, StudentSerializer

class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignatureViewSet(ModelViewSet):
    queryset = Assignature.objects.all()
    serializer_class = AssignatureSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePromotionSerializer
        return PromotionSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
