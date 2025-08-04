from django import forms
import requests
from .models import Library  # Assuming you have a Library model

class LibraryForm(forms.Form):
    student_name = forms.ChoiceField(label="Student")
    book_name = forms.ChoiceField(label="Book")
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        student_api_url = 'http://localhost:9000/api/students/'
        book_api_url = 'http://localhost:7000/api/books/'

        try:
            students = requests.get(student_api_url).json()
            self.fields['student_name'].choices = [(s['name'], s['name']) for s in students]
        except:
            self.fields['student_name'].choices = []

        try:
            books = requests.get(book_api_url).json()
            self.fields['book_name'].choices = [(b['name'], b['name']) for b in books]
        except:
            self.fields['book_name'].choices = []

    def save(self):
        # Assuming you have a Library model that stores this data
        library_instance = Library.objects.create(
            student_name=self.cleaned_data['student_name'],
            book_name=self.cleaned_data['book_name'],
            start_date=self.cleaned_data['start_date'],
            end_date=self.cleaned_data['end_date'],
        )
        return library_instance
