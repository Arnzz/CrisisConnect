from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Dummy data for the disasters
location_data = {
    'Mumbai': {'lat': 19.0760, 'lng': 72.8777, 'disasters': ['Flood', 'Earthquake']},
    'New York': {'lat': 40.7128, 'lng': -74.0060, 'disasters': ['Hurricane']},
    'Tokyo': {'lat': 35.6762, 'lng': 139.6503, 'disasters': ['Earthquake', 'Tsunami']},
    'Singapore': {'lat': 1.3521, 'lng': 103.8198, 'disasters': ['Flood', 'Tsunami']}
}

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    city = request.form['city']

    location = location_data.get(city)
    if not location:
        return "Location not found!", 404

    # Dummy statistics for the selected location
    stats = {
        'weather': 'Sunny',
        'temperature': random.randint(20, 35),
        'wind_speed': random.randint(5, 20),
        'river_flow': random.randint(50, 100),
        'vibrations': random.randint(0, 10)
    }

    return render_template('main.html', name=name, age=age, country=country, city=city, location=location, **stats)

@app.route('/simulate_disaster')
def simulate_disaster():
    disasters = ['Earthquake', 'Flood', 'Tsunami', 'Hurricane']
    disaster = random.choice(disasters)
    return jsonify({'disaster': disaster})

if __name__ == '__main__':
    app.run(debug=True)
