from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, DisciplineViewSet, InstitutionViewSet, TeacherViewSet, StudentViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'disciplines', DisciplineViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
