# Self-Healing Infrastructure — Prometheus + Alertmanager + Ansible

## What this project does
Automatically detects service failures (NGINX down, high CPU) and heals them by running Ansible playbooks via an Alertmanager → webhook → Ansible pipeline.

## Architecture
(prometheus) → (alertmanager) → POST -> webhook (Flask) → runs ansible-playbook -> restarts nginx

## Quick start (tested on Ubuntu 22.04)
1. Clone repo
   ```bash
   git clonne : https://github.com/Moin2811/self-heal-prom-ansible---p-1.git
   cd self-heal-prom-ansible

