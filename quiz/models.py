# models.py - Updated with category support
from django.db import models

class Question(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    
    CATEGORY_CHOICES = (
        ('movies', 'Movies'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('geography', 'Geography'),
        ('history', 'History'),
        ('sports', 'Sports'),
    )
    
    question = models.CharField(max_length=500)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)  # 'A', 'B', 'C', 'D'
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"[{self.category.upper()}] {self.question[:50]}..."
    
    class Meta:
        ordering = ['-created_at']