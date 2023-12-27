
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Employee

# Create your views here.

class EmployeeList(ListView):
    model = Employee

class EmployeeDetail(DetailView):
    model = Employee

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('employee_list')

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')