from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    StudentId  = models.CharField(max_length=50,null=True)
    CourseName = models.CharField(max_length=50,null=True)
    LecturesAttended = models.IntegerField(null=True)
    TotalLectures  = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentName

class Marks(models.Model):
    StudentId  = models.CharField(max_length=50,null=True)
    HomeworkMarks = models.IntegerField(null=True)
    ProjectMarks  = models.IntegerField(null=True)
    QuizzMarks  = models.IntegerField(null=True)
    MidtermMarks  = models.IntegerField(null=True)
    FinalMarks  = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentName

class Notice(models.Model):
    Message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Message
