from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date
from django.views.generic.list import ListView
from employees_app.models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.select_related('department').all()