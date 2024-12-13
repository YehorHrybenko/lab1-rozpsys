from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

SERVICE_PROVIDER_URL = "http://lb-provider:5000/process-data"

def execute_measure_time(action):
    start_time = time.time()
    res = action()
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"### Request time (consumer): {elapsed_time_ms:.2f} ms")

    return res

@app.route("/calculate", methods=["GET"])
def get_data():
    user_data = request.json

    if not user_data:
        return jsonify({"error": "No data provided"}), 400

    try:
        request_data = lambda: requests.get(SERVICE_PROVIDER_URL, json=user_data)
        response = execute_measure_time(request_data)

        response_data = response.json()
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Service provider error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
