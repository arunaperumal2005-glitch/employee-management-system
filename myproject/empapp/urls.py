from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('departments/', views.department_list, name='department_list'),
    path('department/add/', views.department_add, name='department_add'),
    path('department/edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('department/delete/<int:pk>/', views.department_delete, name='department_delete'),
]