from django.urls import path
from . import views

app_name = "quiz_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name='registration'),
    path("Quiz_list", views.page_list, name="page_list"),
    path("Quiz_list/<uuid:id>/", views.quiz_detail, name="quiz_detail"),
    path("Quiz_list/<uuid:id>/update/", views.quiz_update, name="quiz_update"),
    path("Quiz/", views.quiz, name="quiz"),
    path("Quiz_result", views.quiz_result, name="quiz_result")
]