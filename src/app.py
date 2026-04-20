from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/post-data", methods=["POST"])
def post_data():
    try:
        # Ensure request is JSON
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()

        # Validate required fields
        if "name" not in data or not isinstance(data["name"], str):
            return jsonify({"error": "Missing or invalid 'name' field"}), 400

        # Example processing
        response_message = f"Hello, {data['name']}! Your data was received."

        return jsonify({
            "status": "success",
            "message": response_message,
            "received": data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Use PORT environment variable for Code Engine
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
