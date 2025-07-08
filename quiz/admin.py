# admin.py - Updated for better category management
from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_preview', 'category', 'difficulty', 'correct_answer', 'created_at']
    list_filter = ['category', 'difficulty', 'created_at']
    search_fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Question Details', {
            'fields': ('question', 'category', 'difficulty')
        }),
        ('Answer Options', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
        }),
    )
    
    def question_preview(self, obj):
        return obj.question[:50] + "..." if len(obj.question) > 50 else obj.question
    question_preview.short_description = 'Question'
    
    def save_model(self, request, obj, form, change):
        obj.correct_answer = obj.correct_answer.upper()
        super().save_model(request, obj, form, change)