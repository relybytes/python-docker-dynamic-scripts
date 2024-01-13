# Python docker dynamic scripts

## Overview

This repository is a Docker-based solution from Relybytes Srl designed for executing Python scripts dynamically. It allows for script execution via environment variables without the need for traditional building or releasing processes. This tool is particularly useful for developers and system administrators in scenarios requiring quick, adaptable script execution, such as automated tasks or DevOps pipelines.

### Key Features

- **Dynamic Script Execution**: Execute Python scripts directly from environment variables.
- **Cron Job Management**: Schedule script executions efficiently using cron jobs.

## Usage

Details on how to use this Docker image will be provided, including examples for various environments such as Kubernetes, Docker Compose, and VPS setups.

### Docker Compose Example

This example shows how to use the image with Docker Compose:

```yaml
version: "3.8"
services:
  python-app:
    build: .
    environment:
      OS_ADDITIONAL_PACKAGES:
      PIP_REQUIREMENTS:
      CRON_SCHEDULE: "*/1 * * * *"
      SCRIPT_CONTENT: |
        from datetime import datetime
        import some_python_library

        print(f"Current date and time: {datetime.now()}")
```

### Kubernetes Installation Example

To deploy this image in a Kubernetes cluster, use the following configuration as an example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
        - name: python
          image: ghcr.io/relybytes/nginx-certbot:v1.0.0
          env:
            - name: OS_ADDITIONAL_PACKAGES
              value:
            - name: PIP_REQUIREMENTS
              value:
            - name: CRON_SCHEDULE
              value: "*/1 * * * *"
            - name: SCRIPT_CONTENT
              value: |
                from datetime import datetime
                import some_python_library

                print(f"Current date and time: {datetime.now()}")
```

## Table of Contents

1. [Architecture](#architecture)
2. [Repository Structure](#repository-structure)
3. [Installation](#installation)
4. [Build Instructions](#build-instructions)
5. [Running Locally](#running-locally)
6. [Deployment](#deployment)
7. [Testing](#testing)
8. [Further Documentation](#further-documentation)
9. [About the Team](#about-the-team)

## Architecture

This section will provide insights into the architecture of `docker-python-env-script`, demonstrating its adaptability in various scenarios, including Kubernetes clusters, Docker Compose setups, and remote execution on VPS.

## Repository Structure

- **examples/**: Docker-compose examples ready for production.
- **docker-compose.yml**: Local file for testing and building the image.
- **Dockerfile**: Builds the Docker image.
- **requirements.txt**: Lists minimal requirements for basic scripts.
- **execute.py**: Contains the job manager and executor.

## Installation

To develop locally, you need Docker or Docker Compose installed on your machine.

## Build Instructions

Build the image locally using the command: `docker build . -t docker-python-env-script:local`.

## Running Locally

Run the image locally with: `docker-compose up --build`.

## Deployment

For deployment instructions, refer to the `examples` directory in the repository.

## Testing

Test the functionality by running the Docker image and observing the output logs.

## Further Documentation

For guidance on writing Python scripts, visit [Python's Official Tutorial](https://docs.python.org/3/tutorial/index.html). The project is maintained by [Relybytes Srl](www.relybytes.com).
