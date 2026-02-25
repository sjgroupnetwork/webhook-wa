from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

message_logs = []

@app.route("/")
def home():
    return "Webhook aktif bro 🔥"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    nomor = data.get("target")
    status = data.get("status")
    message_id = data.get("id")

    log = {
        "nomor": nomor,
        "status": status,
        "message_id": message_id,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    }

    message_logs.append(log)

    print("Webhook masuk:", log)

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
