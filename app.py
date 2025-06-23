from flask import Flask, request, jsonify
import datetime
import os
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "💬 Hùng's Feedback Server đang hoạt động!"

@app.route("/feedback", methods=["POST"])
def feedback():
    try:
        data = request.get_json(force=True)  # 👈 force=True để ép đọc JSON
        comment = data.get("comment", "").strip()
        if comment:
            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.datetime.now()}] {comment}\n---\n")
            return jsonify({"status": "ok", "message": "Đã nhận góp ý"})
        return jsonify({"status": "fail", "message": "Không có nội dung"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/view-feedback", methods=["GET"])
def view_feedback():
    try:
        if not os.path.exists("feedback.txt"):
            return "<p>⚠️ Chưa có góp ý nào được ghi lại.</p>"

        with open("feedback.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"Không đọc được file: {e}"