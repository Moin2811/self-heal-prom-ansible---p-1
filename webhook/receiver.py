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

@app.route("/health", methods=["GET"])  # for quick checks
def health():
    return "ok", 200

@app.route("/alerts", methods=["POST"])  # Alertmanager webhook target
def alerts():
    data = request.get_json(force=True, silent=True) or {}
    status = data.get("status")  # overall status: firing / resolved
    alerts = data.get("alerts", [])

    actions = []
    for a in alerts:
        labels = a.get("labels", {})
        alertname = labels.get("alertname", "")
        if status == "firing" and alertname in ALERT_TO_PLAYBOOK:
            playbook = ALERT_TO_PLAYBOOK[alertname]
            try:
                # Run: ansible-playbook <playbook>
                # We intentionally don't capture output to keep it simple; check journal logs.
                subprocess.run([
                    "/opt/self-heal/webhook/venv/bin/ansible-playbook",
                    playbook
                ], check=True)
                actions.append({"alert": alertname, "action": "ansible-playbook run", "playbook": playbook})
            except subprocess.CalledProcessError as e:
                actions.append({"alert": alertname, "action": "failed", "error": str(e)})

    return jsonify({"received": True, "status": status, "actions": actions}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
