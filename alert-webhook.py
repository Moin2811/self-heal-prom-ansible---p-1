#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
