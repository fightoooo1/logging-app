from flask import Flask, request
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def index():
    logging.info("=== INCOMING REQUEST ===")
    logging.info(f"Method: {request.method}")
    logging.info(f"Headers: {dict(request.headers)}")
    logging.info(f"Remote addr: {request.remote_addr}")
    return "Logged request\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
