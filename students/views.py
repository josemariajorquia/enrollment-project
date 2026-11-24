from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all().order_by('last_name')
    return render(request, 'student_list.html', {'students': students})


def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_profile.html', {'student': student})


def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form, 'title': 'Add Student'})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_profile', pk=student.pk)
    return render(request, 'student_form.html', {'form': form, 'title': 'Edit Student'})