# devops-final-project

# DevOps Final Project

This repository contains a complete end-to-end DevOps project demonstrating:

- Terraform Infrastructure as Code
- Ansible Configuration Management
- Docker Containerization
- GitHub Actions CI/CD
- AWS Deployment

## Project Structure

#PHASE 1 — Prepare GitHub Repository


https://github.com/anslemdevops/devops-final-project


Create this folder structure locally:


devops-final-project/
│
├── apps/
├── terraform/
├── ansible/
├── screenshots/
├── .github/
│   └── workflows/
└── README.md



# PHASE 2:

PHASE 2 — Create EC2 Instance
Step 1: Launch EC2

AWS Console → EC2 → Launch Instance

Use:

Name: devops-final-project-server
AMI: Amazon Linux 2023
Instance Type: t2.micro
Key Pair: Your existing key pair
Security Group

Allow:

SSH     22      My IP
HTTP    80      Anywhere
Custom  5000    Anywhere
Custom  8080    Anywhere

Launch the instance.

![alt text](screenshots/01-ec2-instance-created.png)


# TASK 3

Connect via SSH

## Phase 1: AWS EC2 Provisioning

### Objective

Provision a cloud server to host the portfolio and Java applications.

### EC2 Configuration

| Setting       | Value                       |
| ------------- | --------------------------- |
| Name          | devops-final-project-server |
| OS            | Amazon Linux 2023           |
| Instance Type | t2.micro                    |

### Security Group

* SSH (22)
* HTTP (80)
* Portfolio App (5000)
* Java App (8080)

### Screenshots

#### EC2 Instance Running

![EC2](screenshots/01-ec2-created.png)

#### SSH Connection

![SSH](screenshots/02-ssh-connected.png)


![alt text](<screenshots/02-ssh connected.png>)

SSH connected

# PHASE 2 - install Docker on EC2

## Phase 2: Docker Installation

### Objective

Install Docker on the EC2 instance to host containerized applications.

### Commands Used

```bash
sudo dnf update -y
sudo dnf install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
newgrp docker
docker ps
```

### Verification

Docker was successfully installed and the Docker service was running.

### Screenshots

#### Docker Installed

![Docker Installed](screenshots/03-docker-installed.png)

#### Docker Service Running

![Docker Running](screenshots/04-docker-running.png)

#### Docker Verification

![Docker PS](screenshots/05-docker-ps.png)


![alt text](screenshots/05-docker-ps.png) 





# Flask Portfolio Application

## Objective

Replace the plain text Flask response with a professional HTML portfolio page using Flask templates.

## Step 1: Create the HTML Template

Created a template file:


templates/index.html


Added the following HTML content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Anslem Iwebor Portfolio</title>
</head>
<body>
    <h1>Welcome to Anslem Iwebor's Portfolio</h1>
    <p>Junior Cloud & DevOps Engineer</p>

    <h2>Skills</h2>
    <ul>
        <li>AWS</li>
        <li>Docker</li>
        <li>Terraform</li>
        <li>Ansible</li>
        <li>GitHub Actions</li>
    </ul>
</body>
</html>
```

## Step 2: Update Flask Application

Modified `app.py` to render the HTML template.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Step 3: Run the Application

Started the Flask application:


python app.py


Application output:


* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000


## Step 4: Verify the Application

Opened the application in a browser:


http://localhost:5000


The portfolio page was displayed successfully.

## Screenshot

![alt text](screenshots/05-flask-portfolio-home.png)




## Installing Git on the EC2 Instance

Git was installed on the Amazon Linux 2023 EC2 instance to enable cloning and managing the project repository directly on the server.

### Install Git


sudo dnf install git -y


### Verify Installation


git --version


### Output

git version <your-version>
```

### Screenshot

![alt text](project/screenshots/06-git-installed-ec2.png)




## Cloning the GitHub Repository

The project repository was cloned from GitHub onto the EC2 instance.

### Clone Repository


git clone https://github.com/anslemdevops/devops-final-project.git



### Verify Repository

ls


### Screenshot

![alt text](screenshots/09-github-repository.png)


![alt text](screenshots/09-github-push-success.png)



# Pushing Changes to GitHub

# Docker Compose Deployment 

## Overview

After creating Docker images for both the Flask Portfolio application and the Java web application, Docker Compose was used to deploy and manage the applications on an Amazon EC2 instance.

The deployment process included:

* Building the Docker images
* Creating and starting containers
* Verifying container health
* Testing application accessibility through a web browser

---

## Building the Applications

The existing containers were stopped and removed before rebuilding the images because there was an error.

### Command


docker compose down
docker compose build --no-cache


### Build Output

The build process successfully created Docker images for both applications.

![alt text](screenshots/11-docker-compose-up.png)



## Starting the Containers

Docker Compose was used to create and start the containers in detached mode.

### Command


docker compose up -d


### Result

* Docker network created successfully
* Portfolio application container started
* Java application container started

**Screenshot**

![alt text](screenshots/11-docker-compose-up.png)

---

## Verifying Running Containers

After deployment, the running containers were verified using Docker.

### Command


docker ps


### Result

Two containers were running successfully:

| Container     | Purpose                     | Port |
| ------------- | --------------------------- | ---- |
| portfolio_app | Flask Portfolio Application | 5000 |
| java_app      | Java Web Application        | 8080 |

**Screenshot**

![alt text](screenshots/12-docker-ps.png)



## Testing the Portfolio Application

The Flask Portfolio application was accessed through the EC2 public IP address.

### URL


http://<44.223.102.157 >:5000


### Verification

The application loaded successfully in the browser, confirming that:

* The Flask application was running correctly
* Docker port mapping was working
* Security group rules allowed inbound traffic

**Screenshot**

![alt text](screenshots/13-portfolio-browser.png)



## Testing the Java Application

The Java application was accessed through the EC2 public IP address.

### URL


http://<44.223.102.157 >:8080


### Verification

The application loaded successfully in the browser, confirming that:

* Tomcat was running correctly
* The application was deployed successfully
* Docker networking and port forwarding were functioning properly

**Screenshot**

![alt text](screenshots/14-java-app-browser.png)



## Deployment Summary

The deployment was completed successfully using Docker Compose on an Amazon EC2 instance.

### Successfully Verified

* Docker images built successfully
* Containers created and started successfully
* Docker networking configured correctly
* Flask Portfolio Application accessible on port 5000
* Java Application accessible on port 8080
* Browser accessibility verified for both applications

This deployment demonstrates the use of containerization and orchestration tools to manage multiple applications in a consistent and repeatable manner.
