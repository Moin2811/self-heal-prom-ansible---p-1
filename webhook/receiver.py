import json
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Path to your Ansible playbook
PLAYBOOK = "/opt/self-heal/ansible/playbooks/restart_nginx.yml"

# Optional: map alert names to different playbooks
ALERT_TO_PLAYBOOK = {
    "BlackboxTargetDown": PLAYBOOK,
    "HostCPUHigh": PLAYBOOK,
}

@app.route("/", methods=["POST"])
def root():
    return "ok", 200

# 🔹 Health endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/alerts", methods=["POST"])  # Alertmanager webhook target
def alerts():
    data = request.get_json(force=True, silent=True) or {}
    status = data.get("status")  # overall status: firing / resolved
    alerts = data.get("alerts", [])

    actions = []
    for a in alerts:
        alertname = a.get("labels", {}).get("alertname")
        playbook = ALERT_TO_PLAYBOOK.get(alertname)
        if playbook:
            try:
                subprocess.run(["ansible-playbook", playbook], check=True)
                actions.append(f"Executed playbook for {alertname}")
            except subprocess.CalledProcessError as e:
                actions.append(f"Failed playbook for {alertname}: {e}")
        else:
            actions.append(f"No playbook mapped for {alertname}")

    return jsonify({"status": status, "actions": actions}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

