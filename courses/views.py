from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from .models import Course, Enrollment

User = get_user_model()

@login_required
def course_list(request):
    if request.user.role == 'student':
        enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('course', flat=True)
        courses = Course.objects.exclude(id__in=enrolled_courses)
    elif request.user.role == 'teacher':
        courses = Course.objects.filter(teacher=request.user)
    else:
        courses = Course.objects.all()

    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('course_detail', course_id=course.id)

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'my_courses.html', {'enrollments': enrollments})

@login_required
def enrolled_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if course.teacher != request.user:
        return HttpResponseForbidden("You are not the teacher of this course.")

    students = User.objects.filter(enrollment__course=course)
    return render(request, 'enrolled_students.html', {'course': course, 'students': students})


@login_required
def my_course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

  
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    if not is_enrolled:
        return HttpResponseForbidden("You are not enrolled in this course.")

    return render(request, 'courses/course_detail.html', {'course': course})


from .models import Assignment, Submission
from .forms import SubmissionForm

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.assignment = assignment
            submission.save()
            return redirect('my_courses')
    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})

@login_required
def grade_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)
    return render(request, 'grade_submissions.html', {'assignment': assignment, 'submissions': submissions})


from django.shortcuts import render
from .models import Course

def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


from django.shortcuts import get_object_or_404

def course_detail_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})
