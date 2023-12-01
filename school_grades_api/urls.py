from rest_framework_nested import routers
from django.urls import path
from school_grades_api import views

router = routers.DefaultRouter()

router.register('assignments', views.AssignmentViewSet)
router.register('assignatures', views.AssignatureViewSet)
router.register('professors', views.ProfessorViewSet)

urlpatterns = router.urls