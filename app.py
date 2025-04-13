from flask import Flask, jsonify
from datetime import datetime, timedelta
from pathlib import Path
import json
import random

app = Flask(__name__)

# Load the Bible reading plan
DIR = Path(__file__).parent
json_path = DIR / 'bible.json'
with open(json_path, 'r') as f:
    reading_plan = json.load(f)

# Optional: Load Bible verses for random verse feature
# You could add a verses.json file with verses
verses_path = DIR / 'verses.json'
try:
    with open(verses_path, 'r') as f:
        bible_verses = json.load(f)
except FileNotFoundError:
    # Sample verses if file doesn't exist
    bible_verses = [
        {"verse": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.", "reference": "John 3:16"},
        {"verse": "I can do all this through him who gives me strength.", "reference": "Philippians 4:13"},
        {"verse": "Trust in the LORD with all your heart and lean not on your own understanding.", "reference": "Proverbs 3:5"},
        {"verse": "For the word of God is alive and active. Sharper than any double-edged sword.", "reference": "Hebrews 4:12"},
        {"verse": "In the beginning God created the heavens and the earth.", "reference": "Genesis 1:1"}
    ]

def generate_link(reading):
    """Generates study links for the reading"""
    if not reading:
        return []
    
    links = []
    reading = reading.lower()
    
    # Handle the case where it's multiple readings separated by semicolons
    if ';' in reading:
        for part in reading.split(';'):
            links.extend(generate_link(part.strip()))
        return links
    
    # Handle the case of 1 John, 2 Peter, etc.
    if reading[0].isdigit() and ' ' in reading:
        reading = reading.replace(' ', '-', 1)
    
    # Split into book and chapters
    parts = reading.split(' ')
    if len(parts) == 1:  # Single chapter book like Philemon
        return [f"https://bible-studys.org/{reading}-chapter-1"]
    
    book = parts[0]
    chapters = parts[1]
    
    # Handle chapter ranges like "1-3"
    if '-' in chapters:
        try:
            start, end = map(int, chapters.split('-'))
            return [f"https://bible-studys.org/{book}-chapter-{i}" for i in range(start, end + 1)]
        except ValueError:
            # Handle special cases or errors
            return [f"https://bible-studys.org/{book}-chapter-{chapters}"]
    
    # Handle single chapter
    return [f"https://bible-studys.org/{book}-chapter-{chapters}"]

@app.route('/api/daily-reading', methods=['GET'])
def get_daily_reading():
    """Returns today's Bible reading plan"""
    start_date = datetime(datetime.now().year, 1, 1)
    
    today = datetime.now()
    day_of_year = (today - start_date).days
    
    # Handle the case if the year has more than 365 days or we're past 365
    if day_of_year >= 365:
        day_of_year = day_of_year % 365
    
    reading = reading_plan[day_of_year]
    links = generate_link(reading)
    
    return jsonify({
        'date': today.strftime('%a, %d %b %Y'),
        'reading': reading,
        'links': links
    })

@app.route('/api/reading/<date_iso>', methods=['GET'])
def get_reading_by_date(date_iso):
    """Returns Bible reading for a specific date (ISO format: YYYY-MM-DD)"""
    try:
        date = datetime.fromisoformat(date_iso)
        start_date = datetime(date.year, 1, 1)
        
        day_of_year = (date - start_date).days
        
        if day_of_year < 0 or day_of_year >= 365:
            return jsonify({'error': 'Date out of range'}), 400
        
        reading = reading_plan[day_of_year]
        links = generate_link(reading)
        
        return jsonify({
            'date': date.strftime('%a, %d %b %Y'),
            'reading': reading,
            'links': links
        })
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

@app.route('/api/random-verse', methods=['GET'])
def get_random_verse():
    """Returns a random Bible verse"""
    verse = random.choice(bible_verses)
    return jsonify(verse)

@app.route('/api/next/<int:days>', methods=['GET'])
def get_next_readings(days):
    """Returns readings for the next N days"""
    if days < 1 or days > 30:  # Limit to 30 days for performance
        return jsonify({'error': 'Days parameter must be between 1 and 30'}), 400
    
    start_date = datetime(datetime.now().year, 1, 1)
    today = datetime.now()
    day_of_year = (today - start_date).days
    
    if day_of_year >= 365:
        day_of_year = day_of_year % 365
    
    readings = []
    for i in range(days):
        future_date = today + timedelta(days=i)
        future_day = (day_of_year + i) % 365
        
        if future_day < len(reading_plan) and reading_plan[future_day]:
            readings.append({
                'date': future_date.strftime('%a, %d %b %Y'),
                'reading': reading_plan[future_day]
            })
    
    return jsonify({
        'next_readings': readings
    })

# Add CORS support
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)