from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from django.http import JsonResponse


@api_view(['GET'])
def course_list_api(request):
    courses = Course.objects.all()
    data = [{"id": course.id, "name": course.name} for course in courses]  # ✅ Use correct field name
    return JsonResponse(data, safe=False)
