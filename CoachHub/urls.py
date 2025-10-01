from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('admin/', views.admin_login, name='admin'),
    path('logout/', views.logout_view, name='logout'),
    path('students/', views.studentdata, name='studentdata'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
]