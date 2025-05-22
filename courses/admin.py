from django.contrib import admin
from .models import Course, Enrollment, Assignment, Submission

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')

admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)
