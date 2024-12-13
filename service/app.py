from flask import Flask, request, jsonify
import time
from calculations import calculations

app = Flask(__name__)

def execute_measure_time(action):
    start_time = time.time()
    res = action()
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"### Calculations time (provider): {elapsed_time_ms:.2f} ms")

    return res

@app.route("/process-data", methods=["GET"])
def process_data():
    received_data = request.json

    if not received_data:
        return jsonify({"error": "No data received"}), 400

    response = execute_measure_time(lambda: calculations(received_data))

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
