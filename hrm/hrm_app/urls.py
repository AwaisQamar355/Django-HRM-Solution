from django.contrib import admin
from django.urls import path,include
from hrm_app import views
urlpatterns = [    
    path('', views.home , name = 'home.html'),
    path('home.html', views.home , name = 'home.html'),
    path('employe_add/', views.employe_add , name = 'employe_add'),
    # path('<int:pk>/delete/', views.employe_delete , name = 'employe_delete'),
    path('employe_list/', views.employe_list , name = 'employe_list'),
    path('employe_update/<int:employe_id>/', views.employe_update , name = 'employe_update'),
    path('<int:pk>/', views.employe_detail , name = 'employe_detail'),
    path('designation_add/', views.designation_add , name = 'designation_add'),
    # path('<int:pk>/detete/', views.designation_delete , name = 'designation_delete'),
    path('designation_list/', views.designation_list , name = 'designation_list'),
    path('designation_update/<int:designation_id>/', views.designation_update, name='designation_update'),
    path('<int:pk>/detail/', views.designation_detail , name = 'designation_detail'),
    path('department_add/', views.department_add , name = 'department_add'),
    # path('<int:pk>/detete/', views.designation_delete , name = 'designation_delete'),
    path('department_list/', views.department_list , name = 'department_list'),
    path('department_update/<int:department_id>/', views.department_update, name='department_update'),
    path('<int:pk>/details/', views.department_detail , name = 'department_detail'),



    path('employe_education/', views.employe_education, name='employe_education'),
    path('employe_entitlement/', views.employe_entitlement, name='employe_entitlement'),
    path('employe_department/', views.employe_department, name='employe_department'),
    path('employe_attendance/', views.employe_attendance, name='employe_attendance'),

    # path('employeeducation_update/<int:employeeducation_id>/', views.employeeducation_update, name='employeeducation_update'),
    path('employeattendance_update/<int:employeattendance_id>/', views.employeattendance_update, name='employeattendance_update'),
    path('employedepartment_update/<int:employedepartment_id>/', views.employedepartment_update, name='employedepartment_update'),
    path('employeentitement_update/<int:employeentitement_id>/', views.employeentitement_update, name='employeentitement_update'),
    path('employeeducation_update/<int:education_id>/', views.employeeducation_update, name='employeeducation_update'),
]



