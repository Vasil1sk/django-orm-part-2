from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentsListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return super().get_queryset().order_by('group')