from rest_framework import serializers
from .models import Library
import requests

class LibrarySerializer(serializers.ModelSerializer):
    # Use ChoiceField to represent the dropdown options
    student_name = serializers.ChoiceField(choices=[])
    book_name = serializers.ChoiceField(choices=[])

    class Meta:
        model = Library
        fields = ['id', 'student_name', 'book_name', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch student and book choices dynamically from APIs
        student_api_url = 'http://localhost:9000/api/students/'
        book_api_url = 'http://localhost:7000/api/books/'

        try:
            students = requests.get(student_api_url).json()
            student_choices = [(s['name'], s['name']) for s in students]
            self.fields['student_name'].choices = student_choices
        except:
            self.fields['student_name'].choices = []

        try:
            books = requests.get(book_api_url).json()
            book_choices = [(b['name'], b['name']) for b in books]
            self.fields['book_name'].choices = book_choices
        except:
            self.fields['book_name'].choices = []
