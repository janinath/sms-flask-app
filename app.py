from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from twilio.rest import Client
import os

# Load .env values
load_dotenv()

app = Flask(__name__)

# Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send-sms", methods=["POST"])
def send_sms():
    data = request.get_json()
    to = data.get("to")
    body = data.get("body")
    print("Using from_:", TWILIO_PHONE_NUMBER, "to:", to, "body:", body)

    try:
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        return jsonify({"success": True, "sid": message.sid})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
