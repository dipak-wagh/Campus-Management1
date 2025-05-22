from django.urls import path
from . import views
from .api import course_list_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('my-courses/<int:course_id>/', views.my_course_detail, name='my_course_detail'),
    path('<int:course_id>/students/', views.enrolled_students, name='enrolled_students'),
    path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('assignment/<int:assignment_id>/grade/', views.grade_submissions, name='grade_submissions'),

  
    path('api/courses/', course_list_api, name='course_list_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
