from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from .serializers import QuestionSerializer
import random

class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        try:
            queryset = Question.objects.all()
            
            # Filter by category if provided
            category = self.request.query_params.get('category', None)
            if category:
                queryset = queryset.filter(category=category)
            
            # Filter by difficulty if provided
            difficulty = self.request.query_params.get('difficulty', None)
            if difficulty:
                queryset = queryset.filter(difficulty=difficulty)
            
            count = int(self.request.query_params.get('count', 5))
            available_count = queryset.count()
            
            if available_count == 0:
                return queryset
            
            count = min(count, available_count)
            question_ids = list(queryset.values_list('id', flat=True))
            random_ids = random.sample(question_ids, count)
            return queryset.filter(id__in=random_ids)
            
        except ValueError:
            return Question.objects.all()[:5]
        except Exception as e:
            print(f"Error in QuestionList: {e}")
            return Question.objects.none()
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                category = request.query_params.get('category', 'any category')
                return Response(
                    {"error": f"No questions available for {category}."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": "An error occurred while fetching questions."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def quiz_page(request):
    return render(request, 'quiz/index.html')

def api_status(request):
    question_count = Question.objects.count()
    category_counts = {}
    
    for category_code, category_name in Question.CATEGORY_CHOICES:
        count = Question.objects.filter(category=category_code).count()
        category_counts[category_code] = {
            'name': category_name,
            'count': count
        }
    
    return JsonResponse({
        'status': 'ok',
        'total_questions': question_count,
        'categories': category_counts,
        'difficulties': ['easy', 'medium', 'hard']
    })

def categories_list(request):
    """Return available categories with question counts"""
    categories = []
    for category_code, category_name in Question.CATEGORY_CHOICES:
        count = Question.objects.filter(category=category_code).count()
        categories.append({
            'code': category_code,
            'name': category_name,
            'count': count
        })
    
    return JsonResponse({'categories': categories})
