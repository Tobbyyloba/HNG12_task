from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime  


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    response = {"email": "samoladapoelisha@gmail.com", "current_datetime": datetime.utcnow().isoformat() + "Z", "github_url": "https://github.com/Tobiloba714/HNG12_task.git"}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)