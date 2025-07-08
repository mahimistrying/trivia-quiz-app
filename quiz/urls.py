# urls.py - Updated with new endpoints
from django.urls import path
from .views import QuestionList, quiz_page, api_status, categories_list

urlpatterns = [
    path('api/questions/', QuestionList.as_view(), name='question-list'),
    path('api/status/', api_status, name='api-status'),
    path('api/categories/', categories_list, name='categories-list'),
    path('quiz/', quiz_page, name='quiz-page'),
    path('', quiz_page, name='home'),
]