# from django.urls import path
# from . import views

# urlpatterns = [
#     path('hello/', views.say_hello)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_student, name='search_student'),
    path('<str:student_id>/', views.student_details, name='student_details')
]
