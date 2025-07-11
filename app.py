
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    routine = [
        {"time": "07:30", "activity": "스트레칭"},
        {"time": "18:00", "activity": "30분 조깅"},
        {"time": "22:30", "activity": "수면 유도 명상"}
    ]
    return jsonify(routine)

if __name__ == '__main__':
    app.run(debug=True)
