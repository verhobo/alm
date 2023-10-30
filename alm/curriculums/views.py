from django.shortcuts import (render, redirect)
from django.http import HttpResponse
from curriculums.models import (Student, Project, Submission)

student_list = [
    'safiyyah',
    'nafisa',
    'amina',
    'ibrahim',
    'meriem',
    'zaynab',
]

def home(request):
    context = {"page_title": "ALM", "students":student_list, "projects": Project.objects.all()}
    return render(request, "main_dir/home_template.html", context)
    #return HttpResponse('Hello, World!')


def coding_class(request):
    context = {"page_title": "Coding", "students":student_list}
    return render(request, "coding_class/main_page.html", context)


def project1(request, student_name):
    context = {"page_title": f"{student_name.capitalize()}'s Project #1",
               "students": student_list}
    return render(request, f"project_1/{student_name}.html", context)


def submit_work(request):
    context = {"page_title": "Submit Work", "students": Student.objects.all(), "projects": Project.objects.all()}
    if request.method == 'POST':
        form = request.POST
        student_id = int(form['student'])
        student = Student.objects.get(pk=student_id)
        project_id = int(form['project'])
        project = Project.objects.get(pk=project_id)
        content = str(form['content'])
        possible_existing_submissions = Submission.objects.filter(name=f"{student.name}'s {project.name}")
        if possible_existing_submissions:
            for existing in possible_existing_submissions:
                existing.delete()
        Submission.objects.create(name=f"{student.name}'s {project.name}",
                                  student=student,
                                  project=project,
                                  content=content)
        return redirect("home")
    return render(request, "submit_work.html", context)


def submissions_list(request):
    context = {"page_title": "Submissions", "submissions":Submission.objects.all()}
    return render(request, "submissions_list.html", context)
