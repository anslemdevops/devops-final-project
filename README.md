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

![alt text](<screenshots/02-ssh connected.png>)

SSH connected

