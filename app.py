from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/soil-moisture')
def soil_moisture():
    return render_template('Soil Live Data/index.html')

@app.route('/weather-forecast')
def weather_forecast():
    return render_template('Pest Detection/templates/upload_file.html')

@app.route('/crop-health')
def crop_health():
    return render_template('Crope Health/templates/index.html')

@app.route('/pest-control')
def pest_control():
    return render_template('pest Control/index.html')

@app.route('/crop-productivity')
def crop_productivity():
    return render_template('C:/Users/acer/Desktop/Tech/Byte Force/Crop Productivity/index.html')

if __name__ == '__main__':
    app.run(debug=True)
