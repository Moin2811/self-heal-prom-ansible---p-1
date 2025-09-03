# Self-Healing Infrastructure — Prometheus + Alertmanager + Ansible

## What this project does
Automatically detects service failures (NGINX down, high CPU) and heals them by running Ansible playbooks via an Alertmanager → webhook → Ansible pipeline.

Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

📌 Project Overview

This project demonstrates a self-healing infrastructure that can automatically detect service failures and recover them using monitoring, alerting, and automation.

🎯 Objective
	•	Detect when a service (e.g., NGINX) goes down or when system metrics cross thresholds.
	•	Trigger an Alertmanager notification.
	•	Execute an Ansible playbook to restart the failed service or system component.

🛠 Tools Used
	•	Prometheus – Monitoring and alerting
	•	Alertmanager – Alert handling and notification
	•	Ansible – Automation for recovery
	•	Ubuntu VM / Docker – Infrastructure setup
	•	Shell Scripting – Automation support

🚀 Steps Involved
	1.	Deploy a sample service (NGINX) for monitoring.
	2.	Configure Prometheus to scrape metrics and set alert rules.
	3.	Connect Prometheus with Alertmanager for handling alerts.
	4.	Configure Alertmanager to trigger a webhook on alerts.
	5.	Create an Ansible playbook to restart the service automatically.
	6.	Validate by simulating a service failure and observing auto-recovery.

📂 Deliverables
	•	Prometheus configuration
	•	Alertmanager webhook setup
	•	Ansible playbook for auto-recovery
	•	Logs/screenshots showing successful self-healing in action

✅ Conclusion

This project highlights how monitoring and automation can be integrated to build resilient and self-healing systems, reducing downtime and ensuring service reliability.

## Architecture
(prometheus) → (alertmanager) → POST -> webhook (Flask) → runs ansible-playbook -> restarts nginx

## Quick start (tested on Ubuntu 22.04)
1. Clone repo
   ```bash
   git clonne : https://github.com/Moin2811/self-heal-prom-ansible---p-1.git
   cd self-heal-prom-ansible


## Screenshots
<img width="1918" height="997" alt="blackbox" src="https://github.com/user-attachments/assets/4132ff82-e4cf-4c6e-a97a-3992a80830c6" />
<img width="1917" height="1008" alt="node exporter" src="https://github.com/user-attachments/assets/e8be01c1-96e9-4707-b30b-861ce9c136d6" />
<img width="1918" height="1005" alt="Screenshot 2025-08-25 173431" src="https://github.com/user-attachments/assets/9b93b03a-139a-487c-8fbe-b7167ef34c73" />
<img width="1918" height="1022" alt="Screenshot 2025-08-25 173529" src="https://github.com/user-attachments/assets/51f5a23d-22a6-455d-9d5e-1bcf8f0e2147" />
<img width="1918" height="1011" alt="Screenshot 2025-08-26 151207" src="https://github.com/user-attachments/assets/da8561d5-86cb-4e01-8a2b-594c443c8c1b" />
<img width="1918" height="1007" alt="Screenshot 2025-08-26 164501" src="https://github.com/user-attachments/assets/a7c1c593-235a-459c-aac3-69c323961a13" />
<img width="1918" height="1016" alt="Screenshot 2025-08-25 173650" src="https://github.com/user-attachments/assets/81d8db5d-b346-454e-9d0e-47da0db26e79" />
<img width="1918" height="1025" alt="Screenshot 2025-08-26 164827" src="https://github.com/user-attachments/assets/a1ff89fc-1e90-4835-a0e5-e33d2110dfc9" />
<img width="1918" height="1006" alt="Screenshot 2025-08-26 164559" src="https://github.com/user-attachments/assets/0e99d90f-51ea-4ebd-9236-8dfce25b9f81" />
<img width="1916" height="1000" alt="Screenshot 2025-08-26 165115" src="https://github.com/user-attachments/assets/46577f8d-fdbe-4236-b5dc-9574d376dafb" />


