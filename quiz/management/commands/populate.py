from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populate database with sample questions for all categories'
    
    def handle(self, *args, **options):
        sample_questions = [
            # Movies
            {
                'question': 'Which movie won the Academy Award for Best Picture in 2020?',
                'option_a': 'Parasite',
                'option_b': '1917',
                'option_c': 'Joker',
                'option_d': 'Once Upon a Time in Hollywood',
                'correct_answer': 'A',
                'difficulty': 'medium',
                'category': 'movies'
            },
            {
                'question': 'Who directed the movie "Inception"?',
                'option_a': 'Steven Spielberg',
                'option_b': 'Christopher Nolan',
                'option_c': 'Martin Scorsese',
                'option_d': 'Quentin Tarantino',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'movies'
            },
            {
                'question': 'Which actor played Jack Dawson in Titanic?',
                'option_a': 'Brad Pitt',
                'option_b': 'Leonardo DiCaprio',
                'option_c': 'Matt Damon',
                'option_d': 'Tom Cruise',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'movies'
            },
            
            # Physics
            {
                'question': 'What is the speed of light in vacuum?',
                'option_a': '3 × 10⁸ m/s',
                'option_b': '3 × 10⁷ m/s',
                'option_c': '3 × 10⁹ m/s',
                'option_d': '3 × 10⁶ m/s',
                'correct_answer': 'A',
                'difficulty': 'medium',
                'category': 'physics'
            },
            {
                'question': 'Who developed the theory of relativity?',
                'option_a': 'Isaac Newton',
                'option_b': 'Albert Einstein',
                'option_c': 'Galileo Galilei',
                'option_d': 'Stephen Hawking',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'physics'
            },
            {
                'question': 'What is the unit of electric current?',
                'option_a': 'Volt',
                'option_b': 'Watt',
                'option_c': 'Ampere',
                'option_d': 'Ohm',
                'correct_answer': 'C',
                'difficulty': 'medium',
                'category': 'physics'
            },
            
            # Chemistry
            {
                'question': 'What is the chemical symbol for gold?',
                'option_a': 'Go',
                'option_b': 'Gd',
                'option_c': 'Au',
                'option_d': 'Ag',
                'correct_answer': 'C',
                'difficulty': 'easy',
                'category': 'chemistry'
            },
            {
                'question': 'What is the pH of pure water?',
                'option_a': '6',
                'option_b': '7',
                'option_c': '8',
                'option_d': '9',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'chemistry'
            },
            {
                'question': 'Which gas makes up about 78% of Earth\'s atmosphere?',
                'option_a': 'Oxygen',
                'option_b': 'Carbon Dioxide',
                'option_c': 'Nitrogen',
                'option_d': 'Argon',
                'correct_answer': 'C',
                'difficulty': 'medium',
                'category': 'chemistry'
            },
            
            # Geography
            {
                'question': 'What is the capital of Australia?',
                'option_a': 'Sydney',
                'option_b': 'Melbourne',
                'option_c': 'Canberra',
                'option_d': 'Perth',
                'correct_answer': 'C',
                'difficulty': 'medium',
                'category': 'geography'
            },
            {
                'question': 'Which is the longest river in the world?',
                'option_a': 'Amazon River',
                'option_b': 'Nile River',
                'option_c': 'Mississippi River',
                'option_d': 'Yangtze River',
                'correct_answer': 'B',
                'difficulty': 'medium',
                'category': 'geography'
            },
            {
                'question': 'Mount Everest is located in which mountain range?',
                'option_a': 'Andes',
                'option_b': 'Rockies',
                'option_c': 'Alps',
                'option_d': 'Himalayas',
                'correct_answer': 'D',
                'difficulty': 'easy',
                'category': 'geography'
            },
            
            # History
            {
                'question': 'In which year did World War II end?',
                'option_a': '1944',
                'option_b': '1945',
                'option_c': '1946',
                'option_d': '1943',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'history'
            },
            {
                'question': 'Who was the first President of the United States?',
                'option_a': 'Thomas Jefferson',
                'option_b': 'Benjamin Franklin',
                'option_c': 'George Washington',
                'option_d': 'John Adams',
                'correct_answer': 'C',
                'difficulty': 'easy',
                'category': 'history'
            },
            {
                'question': 'The Berlin Wall fell in which year?',
                'option_a': '1987',
                'option_b': '1988',
                'option_c': '1989',
                'option_d': '1990',
                'correct_answer': 'C',
                'difficulty': 'medium',
                'category': 'history'
            },
            
            # Sports
            {
                'question': 'How many players are on a basketball team on the court at one time?',
                'option_a': '4',
                'option_b': '5',
                'option_c': '6',
                'option_d': '7',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'sports'
            },
            {
                'question': 'Which country has won the most FIFA World Cups?',
                'option_a': 'Germany',
                'option_b': 'Argentina',
                'option_c': 'Brazil',
                'option_d': 'Italy',
                'correct_answer': 'C',
                'difficulty': 'medium',
                'category': 'sports'
            },
            {
                'question': 'In which sport would you perform a slam dunk?',
                'option_a': 'Tennis',
                'option_b': 'Basketball',
                'option_c': 'Volleyball',
                'option_d': 'Baseball',
                'correct_answer': 'B',
                'difficulty': 'easy',
                'category': 'sports'
            },
        ]
        
        # Clear existing questions
        Question.objects.all().delete()
        
        # Create new questions
        for q_data in sample_questions:
            Question.objects.create(**q_data)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(sample_questions)} sample questions'
            )
        )