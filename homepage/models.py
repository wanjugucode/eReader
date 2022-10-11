from distutils.command.upload import upload
from time import time
from tkinter.tix import Tree
from django.db import models
from datetime import datetime
# Create your models here.
class Course(models.Model):
    course_title=models.CharField(max_length=25 ,null=True)
    course=models.ImageField(null=True)
    date=models.DateTimeField(null=True)
    time=models.DateTimeField(null=True)
class GradeOne(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeTwo(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeThree(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeFour(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeFive(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeSix(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeSeven(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)
class GradeEight(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(null=True)