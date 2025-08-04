from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    student_class = models.IntegerField()
    photo = models.ImageField(upload_to='images/', default='images/default.webp')
    video = models.FileField(upload_to='videos/', default='videos/default.mp4')

    def __str__(self):
        return self.name
