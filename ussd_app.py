import os
from flask import Flask, request
import africastalking

# Initialize the Flask application
app = Flask(__name__)

# Initialize the Africa's Talking SDK
username = "sandbox"  # Your Africa's Talking username
api_key = "f8006883c6f51f13e70a2cf6f8648f409de59f453435923091b087961076f5eb"    # Your Africa's Talking API key

africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        response = "CON Welcome to Mental Health Support\n"
        response += "1. Get mental health tips\n"
        response += "2. Speak to a counselor"
    elif text == "1":
        response = "CON Here are some mental health tips:\n"
        response += "1. Take breaks and relax\n"
        response += "2. Talk about your feelings\n"
        response += "3. Eat well and stay active\n"
        response += "4. Connect with friends and family\n"
        response += "0. Back to main menu"
    elif text == "2":
        response = "CON Connecting you to a counselor. Please hold...\n"
        response += "0. Back to main menu"
        # Send an SMS to connect the user to a counselor
        sms.send("A user needs to talk to a counselor. Phone number: " + phone_number, ["+your_counselor_phone_number"])
    elif text == "1*0" or text == "2*0":
        response = "CON Welcome to Mental Health Support\n"
        response += "1. Get mental health tips\n"
        response += "2. Speak to a counselor"
    else:
        response = "END Thank you for using our service."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
