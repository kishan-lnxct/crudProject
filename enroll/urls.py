from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='add_show'),
    path('student_register', views.student_register, name='student_register'),
    path('delete_record/<int:id>', views.delete_record, name='delete_record'),
    path('<int:id>', views.update_record, name='update_record'),
]