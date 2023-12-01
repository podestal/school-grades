from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Assignment, Assignature, Professor, Promotion
from .serializers import AssignmentSerializer, AssignatureSerializer, ProfessorSerializer, PromotionSerializer

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
    serializer_class = PromotionSerializer

    
