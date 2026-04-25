from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date
from django.views.generic.list import ListView
from employees_app.models import Employee, Department


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        
        return Employee.objects.select_related('department').all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gt3000_employees'] = Employee.objects.filter(salary__gt=3000)
        context['high_earners_count'] = Employee.objects.filter(salary__gte=5000).count()
        
        return context
    