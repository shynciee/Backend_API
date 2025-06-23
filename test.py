import requests

res = requests.post(
    "https://backend-api-znlr.onrender.com/feedback",
    json={"comment": "Test góp ý từ Python"},
    timeout=5
)

print("Status:", res.status_code)
print("Response:", res.text)
