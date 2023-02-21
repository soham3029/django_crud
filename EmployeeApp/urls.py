from django.urls import path
from EmployeeApp import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('department', views.departmentApi),
    path('department/([0-9]+)$', views.departmentApi),
    path('employee', views.employeeApi),
    path('employee/([0-9]+)$', views.employeeApi),
    path('saveFile', views.saveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)