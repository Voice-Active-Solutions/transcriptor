from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/transcription', methods=['POST'])
def receive_transcription():
    try:
        # Ensure request contains JSON
        if not request.is_json:
            return jsonify({"error": "Invalid content type. Expected application/json"}), 400

        data = request.get_json()

        # Validate required field
        if 'transcription' not in data or not isinstance(data['transcription'], str):
            return jsonify({"error": "Missing or invalid 'transcription' field"}), 400

        transcription_text = data['transcription'].strip()

        # Handle empty transcription
        if not transcription_text:
            return jsonify({"error": "Transcription cannot be empty"}), 400

        # Process transcription (example: log it)
        print(f"Received transcription: {transcription_text}")

        # Respond with success
        return jsonify({
            "message": "Transcription received successfully",
            "length": len(transcription_text)
        }), 200

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    # Use PORT environment variable for Code Engine
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
