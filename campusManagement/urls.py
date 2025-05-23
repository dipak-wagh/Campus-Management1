from django.contrib import admin
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),  
    path('register/', views.register_view, name='register'),  
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),  
    path('accounts/', include('accounts.urls')),  
]
