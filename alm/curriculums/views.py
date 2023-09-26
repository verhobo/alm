from django.shortcuts import render
from django.http import HttpResponse

student_list = [
    'safiyyah',
    'nafisa',
    'amina'
]

def home(request):
    context = {"page_title": "ALM", "students":student_list}
    return render(request, "main_dir/home_template.html", context)
    #return HttpResponse('Hello, World!')


def coding_class(request):
    context = {"page_title": "Coding", "students":student_list}
    return render(request, "coding_class/main_page.html", context)


def project1(request, student_name):
    context = {"page_title": f"{student_name.capitalize()}'s Project #1",
               "students": student_list}
    return render(request, f"project_1/{student_name}.html", context)