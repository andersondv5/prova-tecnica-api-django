from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    duration = models.IntegerField(help_text="Duração em semestres")
    
    def __str__(self):
        return f"{self.name} - {self.institution.code}"

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    workload = models.IntegerField(help_text="Carga horária em horas")
    description = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['code', 'course']
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.employee_id}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.student_id}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    class Meta:
        unique_together = ['student', 'discipline']
    
    def __str__(self):
        return f"{self.student} - {self.discipline}"