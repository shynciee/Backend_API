from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "💬 Hùng's Feedback Server đang hoạt động!"

@app.route("/feedback", methods=["POST"])
def receive_feedback():
    data = request.json
    comment = data.get("comment", "").strip()
    if comment:
        with open("feedback.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {comment}\n---\n")
        return jsonify({"status": "ok", "message": "Đã nhận tin."})
    return jsonify({"status": "fail", "message": "Không có nội dung."}), 400
