from flask import Flask, request, jsonify, send_file
from huggingface_hub import InferenceClient
from io import BytesIO
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv, dotenv_values 
import os

app = Flask(__name__)
CORS(app)
load_dotenv() 

client = InferenceClient(
    api_key=os.getenv("API_KEY")
)

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "Default logo prompt")
    
    try:
        image = client.text_to_image(prompt, model="brianling16/logo-lora")
        img_io = BytesIO()
        image.save(img_io, format="PNG")
        img_io.seek(0)
        return send_file(img_io, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
