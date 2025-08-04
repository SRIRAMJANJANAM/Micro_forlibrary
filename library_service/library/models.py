from django.db import models


class Library(models.Model):
    student_name = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.book_name}"
