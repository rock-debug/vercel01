from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from the JSON file
data = [
    {"name": "Xc", "marks": 16}, {"name": "YID", "marks": 1},
    {"name": "xKJA6DzdYa", "marks": 5}, {"name": "L2OxUXo", "marks": 94},
    {"name": "2DgzKyD", "marks": 2}, {"name": "0", "marks": 86},
    {"name": "oePwkJ", "marks": 54}, {"name": "nrP7", "marks": 4},
    {"name": "ygN", "marks": 53}, {"name": "m", "marks": 99},
    {"name": "ig", "marks": 17}, {"name": "1v", "marks": 83},
    {"name": "NgPb", "marks": 69}, {"name": "Axn3RM", "marks": 45},
    {"name": "3", "marks": 42}, {"name": "UTC", "marks": 26},
    {"name": "99Db", "marks": 89}, {"name": "Ulp", "marks": 6},
    {"name": "JOSH", "marks": 22}, {"name": "2", "marks": 59},
    {"name": "zv5", "marks": 71}, {"name": "Sb15iJS90", "marks": 76},
    {"name": "y", "marks": 22}, {"name": "d", "marks": 65},
    {"name": "ChzHcrGai", "marks": 92}, {"name": "0vT4T", "marks": 72},
    {"name": "LF5DigFz", "marks": 25}, {"name": "Sg0V5", "marks": 20},
    {"name": "KOQKgwE", "marks": 13}, {"name": "GzXpzQjjZ", "marks": 23},
    {"name": "TYj", "marks": 95}, {"name": "jZRZ", "marks": 66},
    {"name": "SKZDVdk", "marks": 47}, {"name": "U5whfb", "marks": 60},
    {"name": "XSNrVx", "marks": 20}, {"name": "Ad1e", "marks": 10},
    {"name": "izdUaoDkBF", "marks": 81}, {"name": "pyM3uIEq", "marks": 46},
    {"name": "p0ADrR1b", "marks": 87}, {"name": "5ljbKWvS", "marks": 45},
    {"name": "J2N", "marks": 39}, {"name": "KbGIzN0Col", "marks": 99},
    {"name": "O", "marks": 8}, {"name": "eO6aNDK", "marks": 21},
    {"name": "80mNJCfYs", "marks": 50}, {"name": "wRA4no", "marks": 38},
    {"name": "bHBhyxw39", "marks": 55}, {"name": "PtZU0D", "marks": 1},
    {"name": "ri74bcSQf", "marks": 18}, {"name": "p", "marks": 38},
    {"name": "4fefUdCUlx", "marks": 80}, {"name": "XyJHS3Gi1", "marks": 52},
    {"name": "6LiQK3v", "marks": 69}, {"name": "T0yTLLQY", "marks": 57},
    {"name": "j", "marks": 11}, {"name": "0PKSO", "marks": 15},
    {"name": "O0Tn", "marks": 97}, {"name": "1wB5VBLlo", "marks": 55},
    {"name": "XY", "marks": 85}, {"name": "TVh79LOQ", "marks": 49},
    {"name": "Ldyz0pWMcq", "marks": 41}, {"name": "3Wu", "marks": 44},
    {"name": "ib", "marks": 76}, {"name": "UCA", "marks": 35},
    {"name": "gdzN", "marks": 33}, {"name": "M", "marks": 8},
    {"name": "O4F32tpZ", "marks": 67}, {"name": "qZkaaxqVh9", "marks": 90},
]

# Convert data to a dictionary for fast lookup
data_dict = {student['name']: student['marks'] for student in data}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks_list = [data_dict.get(name, None) for name in names]
    return jsonify({"marks": marks_list})

if __name__ == "__main__":
    app.run(debug=True)

