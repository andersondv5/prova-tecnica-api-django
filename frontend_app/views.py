from django.shortcuts import render
import requests

BACKEND_API = "http://localhost:8000/api/" 

def home(request):
    return render(request, "home.html")

def institutions_list(request):
    r = requests.get(f"{BACKEND_API}institutions/")
    return render(request, "institutions.html", {"items": r.json()})

def courses_list(request):
    r = requests.get(f"{BACKEND_API}courses/")
    return render(request, "courses.html", {"items": r.json()})

def disciplines_list(request):
    r = requests.get(f"{BACKEND_API}disciplines/")
    return render(request, "disciplines.html", {"items": r.json()})

def teachers_list(request):
    r = requests.get(f"{BACKEND_API}teachers/")
    return render(request, "teachers.html", {"items": r.json()})

def students_list(request):
    r = requests.get(f"{BACKEND_API}students/")
    return render(request, "students.html", {"items": r.json()})

def enrollments_list(request):
    r = requests.get(f"{BACKEND_API}enrollments/")
    return render(request, "enrollments.html", {"items": r.json()})
