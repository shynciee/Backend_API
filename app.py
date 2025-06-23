from flask import Flask, request, jsonify
import datetime
import os
from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage

app = Flask(__name__)
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(comment):
    msg = EmailMessage()
    msg["Subject"] = "Góp ý mới từ người dùng"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content(comment)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email đã được gửi!")
    except Exception as e:
        print("Gửi email thất bại:", e)


@app.route("/", methods=["GET"])
def home():
    return "💬 Hùng's Feedback Server đang hoạt động!"


@app.route("/feedback", methods=["POST"])
def feedback():
    
    try:
        data = request.get_json(force=True)
        comment = data.get("comment", "").strip()
        if comment:
            print(f"Góp ý mới: {comment}")
            send_email(comment)  

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
            return "<p>Chưa có góp ý nào được ghi lại.</p>"

        with open("feedback.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"Không đọc được file: {e}"

