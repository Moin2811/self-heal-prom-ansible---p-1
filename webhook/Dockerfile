FROM python:3.9-slim

# Install dependencies and Docker CLI
RUN apt-get update && \
    apt-get install -y curl gnupg2 lsb-release sudo && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean

# Install Python packages
RUN pip install flask requests ansible

WORKDIR /app
COPY webhook_receiver.py /app
COPY restart_nginx.sh /app
RUN chmod +x /app/restart_nginx.sh

CMD ["python", "webhook_receiver.py"]
