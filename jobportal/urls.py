"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index,name = 'index'),
    path('admin_login/', views.admin_login,name = 'admin_login'),
    path('userlogin', views.user_login,name = 'user_login'),
    path('recruiter_login', views.recruiter_login,name = 'recruiter_login'),
    path('user_signup', views.user_signup,name = 'user_signup'),
    path('user_home', views.user_home,name = 'user_home'),
    path('user_logout', views.user_logout,name = 'user_logout'),
    path('recruiter_signup', views.recruiter_signup,name = 'recruiter_signup'),
    path('recruiter_home', views.recruiter_home,name = 'recruiter_home'),
    path('recruiter_home', views.recruiter_home,name = 'recruiter_home'),
    path('admin_home', views.admin_home,name = 'admin_home'),
    path('view_users/', views.view_users,name = 'view_users'),
    path('delete_user/<int:pid>', views.delete_user,name = 'delete_user'),
    path('delete_recruiter/<int:pid>', views.delete_recruiter,name = 'delete_recruiter'),
    path('delete_job/<int:pid>', views.delete_job,name = 'delete_job'),
    path('pending_recruiter', views.pending_recruiter,name = 'pending_recruiter'),
    path('change_status/<int:pid>', views.change_status,name = 'change_status'),
    path('accept_recruiter', views.accept_recruiter,name = 'accept_recruiter'),
    path('reject_recruiter', views.reject_recruiter,name = 'reject_recruiter'),
    path('all_recruiter/', views.all_recruiter,name = 'all_recruiter'),
    path('change_admin_password', views.change_admin_pass,name = 'change_admin_pass'),
    path('user_change_pass', views.user_change_pass,name = 'user_change_pass'),
    path('recruiter_change_pass', views.recruiter_change_pass,name = 'recruiter_change_pass'),
    path('add_job', views.add_job,name = 'add_job'),
    path('job_list/', views.job_list,name = 'job_list'),
    path('user_joblist/', views.user_joblist,name = 'user_joblist'),
    path('edit_jobdetail/<int:pid>', views.edit_job,name = 'edit_jobdetail'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
