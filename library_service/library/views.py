from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibraryForm
from .models import Library
from django.contrib import messages
from rest_framework import viewsets


def library_form_view(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library-list')
    else:
        form = LibraryForm()
    return render(request, 'library_form.html', {'form': form})


def library_list_view(request):
    libraries = Library.objects.all()
    return render(request, 'library_list.html', {'libraries': libraries})


def library_edit_view(request, pk):
    library = get_object_or_404(Library, pk=pk)

    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            # Update the object manually
            library.student_name = form.cleaned_data['student_name']
            library.book_name = form.cleaned_data['book_name']
            library.start_date = form.cleaned_data['start_date']
            library.end_date = form.cleaned_data['end_date']
            library.save()
            return redirect('library-list')
    else:
        form = LibraryForm(initial={
            'student_name': library.student_name,
            'book_name': library.book_name,
            'start_date': library.start_date,
            'end_date': library.end_date,
        })

    return render(request, 'library_form.html', {'form': form, 'edit': True})



def library_delete_view(request, pk):
    library = get_object_or_404(Library, pk=pk)

    if request.method == 'POST':
        library.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('library-list')
    
    # If it's a GET request, simply redirect to the library list without doing anything
    return redirect('library-list')


from .serializers import LibrarySerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def perform_create(self, serializer):
        # Custom handling for creating new library entries
        serializer.save()

    def perform_update(self, serializer):
        # Custom handling for updating library entries
        serializer.save()