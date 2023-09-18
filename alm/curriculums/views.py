from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main_dir/home_template.html")
    #return HttpResponse('Hello, World!')


def coding_class(request):
    context = {}
    return render(request, "coding_class/main_page.html", context)