from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from book import views
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.book_list, name='book_list'),
    path('add/', views.book_form, name='book_form'),
    path('edit/<int:book_id>/', views.book_form, name='book_form'), 
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'), 
]
