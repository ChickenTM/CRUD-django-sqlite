from django.urls import path
from . import views

urlpatterns = [
    path('',views.EmployeeList.as_view(), name='employee_list'),
    path('view/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('new', views.EmployeeCreate.as_view(), name='employee_new'),
    path('edit/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_edit'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),
    
]