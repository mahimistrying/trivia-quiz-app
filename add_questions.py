#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Question

# Clear existing questions
Question.objects.all().delete()

# Comprehensive question database - 120+ questions total
questions = [
    # ================== MOVIES (20 questions) ==================
    {'question': 'Which movie features "May the Force be with you"?', 'option_a': 'Star Trek', 'option_b': 'Star Wars', 'option_c': 'Guardians of the Galaxy', 'option_d': 'Interstellar', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Who directed "Pulp Fiction"?', 'option_a': 'Martin Scorsese', 'option_b': 'Quentin Tarantino', 'option_c': 'Christopher Nolan', 'option_d': 'Steven Spielberg', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'In "The Matrix", what color pill does Neo take?', 'option_a': 'Blue', 'option_b': 'Red', 'option_c': 'Green', 'option_d': 'Yellow', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Which actress played Hermione in Harry Potter?', 'option_a': 'Emma Stone', 'option_b': 'Emma Roberts', 'option_c': 'Emma Watson', 'option_d': 'Emma Thompson', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'What year was "The Godfather" released?', 'option_a': '1970', 'option_b': '1972', 'option_c': '1974', 'option_d': '1976', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Who composed the music for "Jaws"?', 'option_a': 'Hans Zimmer', 'option_b': 'John Williams', 'option_c': 'Danny Elfman', 'option_d': 'Ennio Morricone', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which movie features "My Heart Will Go On"?', 'option_a': 'Titanic', 'option_b': 'The Bodyguard', 'option_c': 'Ghost', 'option_d': 'Dirty Dancing', 'correct_answer': 'A', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'In "Forrest Gump", life is compared to what?', 'option_a': 'A journey', 'option_b': 'A box of chocolates', 'option_c': 'A river', 'option_d': 'A book', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Who directed "Inception"?', 'option_a': 'Steven Spielberg', 'option_b': 'Christopher Nolan', 'option_c': 'Martin Scorsese', 'option_d': 'Ridley Scott', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which movie won Best Picture at the 2020 Oscars?', 'option_a': '1917', 'option_b': 'Joker', 'option_c': 'Parasite', 'option_d': 'Once Upon a Time in Hollywood', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Who played Jack in "Titanic"?', 'option_a': 'Brad Pitt', 'option_b': 'Leonardo DiCaprio', 'option_c': 'Matt Damon', 'option_d': 'Tom Cruise', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Which movie features Jack Sparrow?', 'option_a': 'Treasure Island', 'option_b': 'Pirates of the Caribbean', 'option_c': 'Peter Pan', 'option_d': 'Hook', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Who directed "The Dark Knight"?', 'option_a': 'Tim Burton', 'option_b': 'Christopher Nolan', 'option_c': 'Zack Snyder', 'option_d': 'Sam Raimi', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which movie features "Here\'s looking at you, kid"?', 'option_a': 'Gone with the Wind', 'option_b': 'Casablanca', 'option_c': 'Roman Holiday', 'option_d': 'Sunset Boulevard', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'movies'},
    {'question': 'Who played the Joker in "The Dark Knight"?', 'option_a': 'Jack Nicholson', 'option_b': 'Heath Ledger', 'option_c': 'Joaquin Phoenix', 'option_d': 'Jared Leto', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which animated movie features "Let It Go"?', 'option_a': 'Moana', 'option_b': 'Tangled', 'option_c': 'Frozen', 'option_d': 'Brave', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Who directed "Jaws"?', 'option_a': 'George Lucas', 'option_b': 'Steven Spielberg', 'option_c': 'Francis Ford Coppola', 'option_d': 'Martin Scorsese', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which movie features "I\'ll be back"?', 'option_a': 'Predator', 'option_b': 'The Terminator', 'option_c': 'Total Recall', 'option_d': 'Conan', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'movies'},
    {'question': 'Who played Morpheus in "The Matrix"?', 'option_a': 'Samuel L. Jackson', 'option_b': 'Laurence Fishburne', 'option_c': 'Morgan Freeman', 'option_d': 'James Earl Jones', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'movies'},
    {'question': 'Which movie won the first Best Picture Oscar?', 'option_a': 'Wings', 'option_b': 'Sunrise', 'option_c': 'The Jazz Singer', 'option_d': 'Metropolis', 'correct_answer': 'A', 'difficulty': 'hard', 'category': 'movies'},

    # ================== PHYSICS (20 questions) ==================
    {'question': 'What is gravity on Earth?', 'option_a': '8.8 m/s²', 'option_b': '9.8 m/s²', 'option_c': '10.8 m/s²', 'option_d': '11.8 m/s²', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'Who developed the theory of relativity?', 'option_a': 'Isaac Newton', 'option_b': 'Albert Einstein', 'option_c': 'Niels Bohr', 'option_d': 'Stephen Hawking', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'What is the SI unit of electric current?', 'option_a': 'Volt', 'option_b': 'Watt', 'option_c': 'Ampere', 'option_d': 'Ohm', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Speed of sound in air at room temperature?', 'option_a': '300 m/s', 'option_b': '343 m/s', 'option_c': '400 m/s', 'option_d': '500 m/s', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Which law: energy cannot be created or destroyed?', 'option_a': 'Newton\'s First Law', 'option_b': 'Conservation of Energy', 'option_c': 'Ohm\'s Law', 'option_d': 'Hooke\'s Law', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'What particle has no electric charge?', 'option_a': 'Proton', 'option_b': 'Electron', 'option_c': 'Neutron', 'option_d': 'Ion', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'Formula for kinetic energy?', 'option_a': 'KE = mv', 'option_b': 'KE = ½mv²', 'option_c': 'KE = m²v', 'option_d': 'KE = mv²', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Why does the sky appear blue?', 'option_a': 'Refraction', 'option_b': 'Reflection', 'option_c': 'Rayleigh scattering', 'option_d': 'Absorption', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'physics'},
    {'question': 'Unit of frequency?', 'option_a': 'Joule', 'option_b': 'Hertz', 'option_c': 'Newton', 'option_d': 'Pascal', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'Who formulated the three laws of motion?', 'option_a': 'Galileo Galilei', 'option_b': 'Isaac Newton', 'option_c': 'Albert Einstein', 'option_d': 'Johannes Kepler', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'What is the speed of light in vacuum?', 'option_a': '3 × 10⁸ m/s', 'option_b': '3 × 10⁷ m/s', 'option_c': '3 × 10⁹ m/s', 'option_d': '3 × 10⁶ m/s', 'correct_answer': 'A', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Unit of electric resistance?', 'option_a': 'Ampere', 'option_b': 'Volt', 'option_c': 'Ohm', 'option_d': 'Watt', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Which force keeps planets in orbit?', 'option_a': 'Electromagnetic', 'option_b': 'Gravitational', 'option_c': 'Nuclear', 'option_d': 'Centrifugal', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'What is absolute zero in Celsius?', 'option_a': '-273.15°C', 'option_b': '-373.15°C', 'option_c': '-173.15°C', 'option_d': '-200°C', 'correct_answer': 'A', 'difficulty': 'hard', 'category': 'physics'},
    {'question': 'Formula for power?', 'option_a': 'P = VI', 'option_b': 'P = I²R', 'option_c': 'P = V²/R', 'option_d': 'All of the above', 'correct_answer': 'D', 'difficulty': 'hard', 'category': 'physics'},
    {'question': 'Which scientist discovered radioactivity?', 'option_a': 'Marie Curie', 'option_b': 'Henri Becquerel', 'option_c': 'Pierre Curie', 'option_d': 'Ernest Rutherford', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'physics'},
    {'question': 'Unit of work or energy?', 'option_a': 'Newton', 'option_b': 'Joule', 'option_c': 'Watt', 'option_d': 'Pascal', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'physics'},
    {'question': 'Which law describes electromagnetic induction?', 'option_a': 'Coulomb\'s Law', 'option_b': 'Faraday\'s Law', 'option_c': 'Ohm\'s Law', 'option_d': 'Gauss\'s Law', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'physics'},
    {'question': 'What determines the color of light?', 'option_a': 'Amplitude', 'option_b': 'Frequency', 'option_c': 'Speed', 'option_d': 'Intensity', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'physics'},
    {'question': 'Unit of magnetic field strength?', 'option_a': 'Tesla', 'option_b': 'Weber', 'option_c': 'Henry', 'option_d': 'Gauss', 'correct_answer': 'A', 'difficulty': 'hard', 'category': 'physics'},

    # ================== CHEMISTRY (20 questions) ==================
    {'question': 'What is the chemical symbol for sodium?', 'option_a': 'S', 'option_b': 'So', 'option_c': 'Na', 'option_d': 'N', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'What is the pH of pure water?', 'option_a': '6', 'option_b': '7', 'option_c': '8', 'option_d': '9', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'How many electrons does a carbon atom have?', 'option_a': '4', 'option_b': '6', 'option_c': '8', 'option_d': '12', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Most abundant gas in Earth\'s atmosphere?', 'option_a': 'Oxygen', 'option_b': 'Carbon dioxide', 'option_c': 'Nitrogen', 'option_d': 'Argon', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Which element has the highest electronegativity?', 'option_a': 'Oxygen', 'option_b': 'Fluorine', 'option_c': 'Chlorine', 'option_d': 'Nitrogen', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'chemistry'},
    {'question': 'Chemical formula for water?', 'option_a': 'H2O', 'option_b': 'HO2', 'option_c': 'H3O', 'option_d': 'H2O2', 'correct_answer': 'A', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Which gas is produced when metals react with acids?', 'option_a': 'Oxygen', 'option_b': 'Carbon dioxide', 'option_c': 'Hydrogen', 'option_d': 'Nitrogen', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Atomic number of oxygen?', 'option_a': '6', 'option_b': '7', 'option_c': '8', 'option_d': '16', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Which bond forms when electrons are shared?', 'option_a': 'Ionic bond', 'option_b': 'Covalent bond', 'option_c': 'Metallic bond', 'option_d': 'Hydrogen bond', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Lightest element in the periodic table?', 'option_a': 'Helium', 'option_b': 'Hydrogen', 'option_c': 'Lithium', 'option_d': 'Carbon', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Chemical symbol for gold?', 'option_a': 'Go', 'option_b': 'Gd', 'option_c': 'Au', 'option_d': 'Ag', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Which gas makes up about 21% of air?', 'option_a': 'Nitrogen', 'option_b': 'Oxygen', 'option_c': 'Carbon dioxide', 'option_d': 'Argon', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Chemical formula for table salt?', 'option_a': 'NaCl', 'option_b': 'KCl', 'option_c': 'CaCl2', 'option_d': 'MgCl2', 'correct_answer': 'A', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Which element has the symbol Fe?', 'option_a': 'Fluorine', 'option_b': 'Iron', 'option_c': 'Francium', 'option_d': 'Fermium', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Number of valence electrons in carbon?', 'option_a': '2', 'option_b': '4', 'option_c': '6', 'option_d': '8', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Which acid is in vinegar?', 'option_a': 'Citric acid', 'option_b': 'Acetic acid', 'option_c': 'Hydrochloric acid', 'option_d': 'Sulfuric acid', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'What turns litmus paper red?', 'option_a': 'Base', 'option_b': 'Acid', 'option_c': 'Neutral solution', 'option_d': 'Salt', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'chemistry'},
    {'question': 'Which noble gas is most abundant?', 'option_a': 'Helium', 'option_b': 'Neon', 'option_c': 'Argon', 'option_d': 'Krypton', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'chemistry'},
    {'question': 'Chemical formula for methane?', 'option_a': 'CH4', 'option_b': 'C2H6', 'option_c': 'C2H4', 'option_d': 'C3H8', 'correct_answer': 'A', 'difficulty': 'medium', 'category': 'chemistry'},
    {'question': 'Which element is a liquid at room temperature?', 'option_a': 'Gallium', 'option_b': 'Mercury', 'option_c': 'Bromine', 'option_d': 'Both B and C', 'correct_answer': 'D', 'difficulty': 'hard', 'category': 'chemistry'},

    # ================== GEOGRAPHY (20 questions) ==================
    {'question': 'What is the capital of Japan?', 'option_a': 'Osaka', 'option_b': 'Kyoto', 'option_c': 'Tokyo', 'option_d': 'Hiroshima', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'geography'},
    {'question': 'Which is the largest continent?', 'option_a': 'Africa', 'option_b': 'Asia', 'option_c': 'North America', 'option_d': 'Europe', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'geography'},
    {'question': 'Which mountain range contains Mount Everest?', 'option_a': 'Andes', 'option_b': 'Rockies', 'option_c': 'Alps', 'option_d': 'Himalayas', 'correct_answer': 'D', 'difficulty': 'easy', 'category': 'geography'},
    {'question': 'Longest river in the world?', 'option_a': 'Amazon', 'option_b': 'Nile', 'option_c': 'Mississippi', 'option_d': 'Yangtze', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Which country has the most time zones?', 'option_a': 'United States', 'option_b': 'Russia', 'option_c': 'China', 'option_d': 'Canada', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Smallest country in the world?', 'option_a': 'Monaco', 'option_b': 'San Marino', 'option_c': 'Vatican City', 'option_d': 'Liechtenstein', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Largest desert in the world?', 'option_a': 'Sahara', 'option_b': 'Gobi', 'option_c': 'Antarctica', 'option_d': 'Arabian', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Capital of Australia?', 'option_a': 'Sydney', 'option_b': 'Melbourne', 'option_c': 'Canberra', 'option_d': 'Perth', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Capital of Brazil?', 'option_a': 'Rio de Janeiro', 'option_b': 'São Paulo', 'option_c': 'Brasília', 'option_d': 'Salvador', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Largest ocean?', 'option_a': 'Atlantic', 'option_b': 'Pacific', 'option_c': 'Indian', 'option_d': 'Arctic', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'geography'},
    {'question': 'Which country is shaped like a boot?', 'option_a': 'Spain', 'option_b': 'Italy', 'option_c': 'Greece', 'option_d': 'Portugal', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'geography'},
    {'question': 'Highest waterfall in the world?', 'option_a': 'Niagara Falls', 'option_b': 'Victoria Falls', 'option_c': 'Angel Falls', 'option_d': 'Iguazu Falls', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Which city straddles two continents?', 'option_a': 'Cairo', 'option_b': 'Istanbul', 'option_c': 'Moscow', 'option_d': 'Suez', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Capital of Canada?', 'option_a': 'Toronto', 'option_b': 'Vancouver', 'option_c': 'Montreal', 'option_d': 'Ottawa', 'correct_answer': 'D', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Which African country was never colonized?', 'option_a': 'Ethiopia', 'option_b': 'Liberia', 'option_c': 'Morocco', 'option_d': 'Both A and B', 'correct_answer': 'D', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Deepest point on Earth?', 'option_a': 'Dead Sea', 'option_b': 'Mariana Trench', 'option_c': 'Grand Canyon', 'option_d': 'Death Valley', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Which country has the most natural lakes?', 'option_a': 'United States', 'option_b': 'Russia', 'option_c': 'Canada', 'option_d': 'Finland', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Capital of South Africa?', 'option_a': 'Johannesburg', 'option_b': 'Cape Town', 'option_c': 'Pretoria', 'option_d': 'All of the above', 'correct_answer': 'D', 'difficulty': 'hard', 'category': 'geography'},
    {'question': 'Which sea is the saltiest?', 'option_a': 'Dead Sea', 'option_b': 'Red Sea', 'option_c': 'Mediterranean Sea', 'option_d': 'Black Sea', 'correct_answer': 'A', 'difficulty': 'medium', 'category': 'geography'},
    {'question': 'Which country is known as the Land of Rising Sun?', 'option_a': 'China', 'option_b': 'Japan', 'option_c': 'South Korea', 'option_d': 'Thailand', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'geography'},

    # ================== HISTORY (20 questions) ==================
    {'question': 'Who was the first person on the moon?', 'option_a': 'Buzz Aldrin', 'option_b': 'Neil Armstrong', 'option_c': 'John Glenn', 'option_d': 'Alan Shepard', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'In which year did the Berlin Wall fall?', 'option_a': '1987', 'option_b': '1988', 'option_c': '1989', 'option_d': '1990', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Which ancient wonder was in Alexandria?', 'option_a': 'Hanging Gardens', 'option_b': 'Colossus of Rhodes', 'option_c': 'Lighthouse of Alexandria', 'option_d': 'Temple of Artemis', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'history'},
    {'question': 'Who painted the Sistine Chapel ceiling?', 'option_a': 'Leonardo da Vinci', 'option_b': 'Michelangelo', 'option_c': 'Raphael', 'option_d': 'Donatello', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Which war was fought between 1914-1918?', 'option_a': 'World War II', 'option_b': 'World War I', 'option_c': 'Korean War', 'option_d': 'Vietnam War', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'First President of the United States?', 'option_a': 'Thomas Jefferson', 'option_b': 'John Adams', 'option_c': 'George Washington', 'option_d': 'Benjamin Franklin', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'In which year did the Titanic sink?', 'option_a': '1910', 'option_b': '1912', 'option_c': '1914', 'option_d': '1916', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Which empire was ruled by Julius Caesar?', 'option_a': 'Greek Empire', 'option_b': 'Roman Empire', 'option_c': 'Persian Empire', 'option_d': 'Egyptian Empire', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'When did the American Civil War end?', 'option_a': '1863', 'option_b': '1864', 'option_c': '1865', 'option_d': '1866', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Which country gifted the Statue of Liberty?', 'option_a': 'England', 'option_b': 'Spain', 'option_c': 'France', 'option_d': 'Italy', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'When did World War II end?', 'option_a': '1944', 'option_b': '1945', 'option_c': '1946', 'option_d': '1947', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'Who wrote "I Have a Dream" speech?', 'option_a': 'Malcolm X', 'option_b': 'Martin Luther King Jr.', 'option_c': 'John F. Kennedy', 'option_d': 'Abraham Lincoln', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'Which year did the Holocaust end?', 'option_a': '1944', 'option_b': '1945', 'option_c': '1946', 'option_d': '1947', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Who was the first female ruler of Egypt?', 'option_a': 'Cleopatra', 'option_b': 'Nefertiti', 'option_c': 'Hatshepsut', 'option_d': 'Ankhesenamun', 'correct_answer': 'C', 'difficulty': 'hard', 'category': 'history'},
    {'question': 'Which year did the Soviet Union collapse?', 'option_a': '1989', 'option_b': '1990', 'option_c': '1991', 'option_d': '1992', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Who discovered America?', 'option_a': 'Vasco da Gama', 'option_b': 'Christopher Columbus', 'option_c': 'Ferdinand Magellan', 'option_d': 'Marco Polo', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'history'},
    {'question': 'Which ancient city was destroyed by a volcano?', 'option_a': 'Troy', 'option_b': 'Pompeii', 'option_c': 'Carthage', 'option_d': 'Babylon', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Who was the last Tsar of Russia?', 'option_a': 'Nicholas I', 'option_b': 'Nicholas II', 'option_c': 'Alexander III', 'option_d': 'Peter the Great', 'correct_answer': 'B', 'difficulty': 'hard', 'category': 'history'},
    {'question': 'In which year did India gain independence?', 'option_a': '1946', 'option_b': '1947', 'option_c': '1948', 'option_d': '1949', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},
    {'question': 'Who was known as the Iron Lady?', 'option_a': 'Queen Elizabeth II', 'option_b': 'Margaret Thatcher', 'option_c': 'Indira Gandhi', 'option_d': 'Golda Meir', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'history'},

    # ================== SPORTS (20 questions) ==================
    {'question': 'How many players on a basketball court per team?', 'option_a': '4', 'option_b': '5', 'option_c': '6', 'option_d': '7', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'Which country won the most FIFA World Cups?', 'option_a': 'Germany', 'option_b': 'Argentina', 'option_c': 'Brazil', 'option_d': 'Italy', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'In which sport do you slam dunk?', 'option_a': 'Tennis', 'option_b': 'Basketball', 'option_c': 'Volleyball', 'option_d': 'Baseball', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'How many holes in a standard golf round?', 'option_a': '9', 'option_b': '18', 'option_c': '27', 'option_d': '36', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'Who holds the record for most Olympic golds?', 'option_a': 'Carl Lewis', 'option_b': 'Mark Spitz', 'option_c': 'Michael Phelps', 'option_d': 'Usain Bolt', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'Maximum score in bowling?', 'option_a': '200', 'option_b': '250', 'option_c': '300', 'option_d': '350', 'correct_answer': 'C', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'In tennis, what does "love" mean?', 'option_a': 'A tie', 'option_b': 'Zero points', 'option_c': 'A perfect shot', 'option_d': 'Match point', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'Which sport is "America\'s pastime"?', 'option_a': 'Football', 'option_b': 'Basketball', 'option_c': 'Baseball', 'option_d': 'Hockey', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'How long is a marathon?', 'option_a': '25.2 miles', 'option_b': '26.2 miles', 'option_c': '27.2 miles', 'option_d': '28.2 miles', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'Which sport has 11 players per side?', 'option_a': 'Basketball', 'option_b': 'Soccer', 'option_c': 'Volleyball', 'option_d': 'Hockey', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'In which sport is "love" a score?', 'option_a': 'Tennis', 'option_b': 'Badminton', 'option_c': 'Squash', 'option_d': 'All of the above', 'correct_answer': 'D', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'How many periods in ice hockey?', 'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'What is a perfect score in gymnastics?', 'option_a': '9', 'option_b': '10', 'option_c': '100', 'option_d': 'No perfect score', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'In which sport do you use a puck?', 'option_a': 'Field hockey', 'option_b': 'Ice hockey', 'option_c': 'Lacrosse', 'option_d': 'Polo', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'How many Grand Slam tournaments in tennis?', 'option_a': '3', 'option_b': '4', 'option_c': '5', 'option_d': '6', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'In American football, how many points is a touchdown?', 'option_a': '3', 'option_b': '6', 'option_c': '7', 'option_d': '8', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'Which Olympic sport uses a shuttlecock?', 'option_a': 'Tennis', 'option_b': 'Badminton', 'option_c': 'Squash', 'option_d': 'Table tennis', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'How many rings on the Olympic flag?', 'option_a': '4', 'option_b': '5', 'option_c': '6', 'option_d': '7', 'correct_answer': 'B', 'difficulty': 'easy', 'category': 'sports'},
    {'question': 'In golf, what is one stroke under par called?', 'option_a': 'Eagle', 'option_b': 'Birdie', 'option_c': 'Bogey', 'option_d': 'Albatross', 'correct_answer': 'B', 'difficulty': 'medium', 'category': 'sports'},
    {'question': 'Which country hosted the 2016 Olympics?', 'option_a': 'China', 'option_b': 'United Kingdom', 'option_c': 'Brazil', 'option_d': 'Russia', 'correct_answer': 'C', 'difficulty': 'easy', 'category': 'sports'},
]

# Create all questions
for q in questions:
    Question.objects.create(**q)

print(f"Successfully added {len(questions)} comprehensive questions!")
print("Question breakdown by category:")
for category in ['movies', 'physics', 'chemistry', 'geography', 'history', 'sports']:
    count = Question.objects.filter(category=category).count()
    print(f"  {category.title()}: {count} questions")

print("Difficulty breakdown:")
for difficulty in ['easy', 'medium', 'hard']:
    count = Question.objects.filter(difficulty=difficulty).count()
    print(f"  {difficulty.title()}: {count} questions")
