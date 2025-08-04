from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from student import views 
router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.student_list, name='student_list'),
    path('add/', views.student_form, name='student_form'),
    path('edit/<int:student_id>/', views.student_form, name='student_form'), 
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),  
]
