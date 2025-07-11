from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/recommend")
def recommend():
    return jsonify({
        "routines": [
            {"time": "07:30", "task": "가벼운 스트레칭", "reason": "아침형 인간 + 운동 목표"},
            {"time": "18:00", "task": "30분 조깅", "reason": "유사 사용자 성공률 85%"},
            {"time": "22:30", "task": "수면 유도 명상", "reason": "취침 전 안정 패턴"}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
