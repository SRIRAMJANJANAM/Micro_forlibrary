from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# DRF router for API
router = DefaultRouter()
router.register(r'api/library', LibraryViewSet, basename='library')

urlpatterns = [
    path('library/', library_list_view, name='library-list'),
    path('library/add/', library_form_view, name='library-add'),
    path('library/edit/<int:pk>/', library_edit_view, name='library-edit'),
    path('library/delete/<int:pk>/', library_delete_view, name='library-delete'),
    
    # API endpoints
    path('', include(router.urls)),
]
