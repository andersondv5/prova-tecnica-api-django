from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('institutions/', views.institutions_list, name='institutions_list'),
    path('courses/', views.courses_list, name='courses_list'),
    path('disciplines/', views.disciplines_list, name='disciplines_list'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('students/', views.students_list, name='students_list'),
    path('enrollments/', views.enrollments_list, name='enrollments_list'),
]
