from django.db import models

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=8000)


class Student(models.Model):

    name = models.CharField(max_length=80)

class Submission(models.Model):

    name=models.CharField(unique=False, max_length=250)

    student = models.ForeignKey(Student, related_name="submissions", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="submissions", on_delete=models.CASCADE)
    content = models.CharField(max_length=150)  #todo make this more complicated at some point -- maybe it's a html document that gets uploaded?