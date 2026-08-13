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
