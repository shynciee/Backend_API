import requests

url = "https://backend-api-znlr.onrender.com/view-feedback"

try:
    response = requests.get(url, timeout=5)
    print("Status:", response.status_code)
    print("Nội dung góp ý nhận được:\n")
    print(response.text)
except Exception as e:
    print("Lỗi khi gọi API:", e)
