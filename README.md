🧠 Trivia Quiz Hub
A modern, responsive web-based trivia quiz application built with Django and vanilla JavaScript. Challenge yourself with questions from multiple categories including movies, science, history, and sports!

✨ Features

🎬 Multiple Categories: Movies, Physics, Chemistry, Geography, History, Sports
🎨 Modern UI: Beautiful, responsive design with smooth animations
📊 Progress Tracking: Real-time progress bar and scoring
💡 Instant Feedback: Immediate feedback on answers with correct/incorrect highlighting
📱 Mobile Friendly: Works seamlessly on desktop, tablet, and mobile devices
⚡ Fast Performance: Optimized loading and smooth transitions
🔧 Admin Panel: Easy question management through Django admin

🚀 Live Demo
View Live Demo (Update this with your actual deployment URL)
🛠️ Tech Stack

Backend: Django 5.2.3, Django REST Framework
Frontend: HTML5, CSS3, Vanilla JavaScript
Database: SQLite (easily upgradeable to PostgreSQL)
Styling: Custom CSS with modern design principles
API: RESTful API architecture

📋 Prerequisites

Python 3.8+
pip
Git

🔧 Installation & Setup

Clone the repository
bashgit clone https://github.com/YOUR_USERNAME/trivia-quiz-app.git
cd trivia-quiz-app

Create virtual environment
bashpython -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

Install dependencies
bashpip install -r requirements.txt

Run migrations
bashpython manage.py makemigrations
python manage.py migrate

Create sample questions (optional)
bashpython manage.py shell
# Then run the sample questions script from the documentation

Create superuser (optional)
bashpython manage.py createsuperuser

Start development server
bashpython manage.py runserver

Visit the app
Open http://127.0.0.1:8000 in your browser

📁 Project Structure
trivia-quiz/
├── quiz_project/          # Django project settings
├── quiz/                  # Main quiz application
│   ├── templates/         # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # API views and logic
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin configuration
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
🎮 How to Play

Choose a Category: Select from Movies, Science topics, History, or Sports
Answer Questions: Click on your choice from multiple options
Get Instant Feedback: See if you're right or wrong immediately
Track Progress: Watch your progress bar and score
View Results: Get your final score and performance message
Try Again: Retry the same category or try a different one

🔧 API Endpoints

GET /api/questions/?category={category}&count={number} - Get random questions
GET /api/status/ - Get category information and question counts
GET /api/categories/ - Get all available categories

🎨 Categories Available

🎬 Movies: Film trivia, actors, directors, cinema history
⚛️ Physics: Laws of motion, energy, matter, universe
🧪 Chemistry: Elements, compounds, reactions, molecular structures
🌍 Geography: Countries, capitals, landmarks, natural phenomena
🏛️ History: Historical events, figures, ancient to modern times
⚽ Sports: Athletes, teams, sporting events, Olympics

👨‍💻 Development
Adding New Questions

Use the Django admin panel at /admin/
Or use the Django shell:
pythonfrom quiz.models import Question
Question.objects.create(
    question="Your question here?",
    option_a="Option A",
    option_b="Option B", 
    option_c="Option C",
    option_d="Option D",
    correct_answer="A",  # A, B, C, or D
    difficulty="easy",   # easy, medium, hard
    category="movies"    # movies, physics, chemistry, etc.
)


Adding New Categories

Update CATEGORY_CHOICES in models.py
Update the frontend category configurations
Run migrations and add questions for the new category

🚀 Deployment
This app can be easily deployed to:

Render (Recommended - Free tier available)
Railway
Heroku
Vercel (Frontend + API)
PythonAnywhere

See deployment guides in the docs/ folder.
🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

Built with Django and Django REST Framework
UI inspired by modern web design principles
Icons and emojis for enhanced user experience

📧 Contact
Your Name - your.email@example.com
Project Link: https://github.com/YOUR_USERNAME/trivia-quiz-app

⭐ Star this repository if you found it helpful!
