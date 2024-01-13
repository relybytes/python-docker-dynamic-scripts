FROM python:3.9-slim

WORKDIR /app

# Copy the shell script and make it executable
COPY install_requirements.sh .
COPY execute.py .
RUN chmod +x install_requirements.sh

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt


# Run the shell script to install requirements
CMD ["./install_requirements.sh"]
