from flask import Flask, request, jsonify
from collections import deque
import threading
import time

app = Flask(__name__)

datatable = deque()
current_value = None

INTERVAL = 0.1  # Seconds between values

def process_queue():
    global current_value

    while True:
        if datatable:
            current_value = datatable.popleft()
            print("Sending:", current_value)

        time.sleep(INTERVAL)

threading.Thread(target=process_queue, daemon=True).start()

@app.route("/")
def home():
    return "Python server is online!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    user_input = data["value"]

    for value in user_input.split():
        datatable.append(value)

    return jsonify({"status": "received"})


@app.route("/next", methods=["GET"])
def next_value():
    global current_value

    value = current_value
    current_value = None

    return jsonify({"value": value})
