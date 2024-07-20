

# 🌐 VPC Setup with Multi-AZ Applications & Load Balancing

## 📋 Prerequisites

Before you start, ensure you have:

- **AWS Account**: An IAM user with permissions for S3, EC2, VPC, Load Balancer, and Admin access.
- **VS Code**: Use GitHub Codespaces if VS Code is not installed locally.
- **Terraform**: Installed for managing infrastructure.
## 🗂️ Table of Contents

1. [Project Overview](#-project-overview)
2. [Getting Started](#-getting-started)
   - [Set Up IAM User](#1-set-up-iam-user)
   - [Configure Development Environment](#2-configure-development-environment)
   - [AWS Configuration](#3-aws-configuration)
   - [Initialize Terraform](#4-initialize-terraform)
   - [Define Infrastructure](#5-define-infrastructure)
   - [Deploy Resources](#6-deploy-resources)
   - [S3 Bucket Setup](#7-s3-bucket-setup)
   - [Launch EC2 Instances](#8-launch-ec2-instances)
   - [Access Verification](#9-access-verification)
   - [Configure Load Balancer](#10-configure-load-balancer)
   - [Outputs](#11-outputs)
   - [Validate and Apply](#12-validate-and-apply)
3. [Challenges Faced](#-challenges-faced)
4. [Final Notes](#-final-notes)

## 🛠️ Project Overview

This project sets up a **Virtual Private Cloud (VPC)**, deploys **2 applications** in different Availability Zones, and creates a **load balancer** to distribute traffic between instances automatically. By distributing resources across multiple Availability Zones, the application achieves high availability and auto-scaling capabilities, ensuring continuous operation even if one zone fails.
# 🚀 Getting Started

### 1. Set Up IAM User

Create an IAM user with the following permissions:
- **S3**
- **EC2**
- **VPC**
- **Load Balancer**
- **Admin**

### 2. Configure Development Environment

- **VS Code**: If not using VS Code locally, activate GitHub Codespaces. Locate the Dev Configuration file and set up the environment.
- **Terraform**: Add the necessary `tf` files and configure AWS credentials in your Codespaces.

### 3. AWS Configuration

- **Access Keys**: Go to AWS Security Credentials, create an access key, and configure AWS in Codespaces using `aws configure`. Enter your Access Key, Secret Key, region, and output format.

### 4. Initialize Terraform

- Create a project folder and set up the Terraform provider for AWS.
- Run `terraform init` to initialize the working directory and verify Terraform's connection to AWS.

### 5. Define Infrastructure

- **VPC**: Create a Virtual Private Cloud (VPC) with a unique CIDR block.
- **Subnets**: Define two subnets in different Availability Zones.
- **Internet Gateway**: Attach it to the VPC for internet access.
- **Route Table**: Define routing rules and associate it with the subnets.
- **Security Groups**: Configure inbound and outbound rules for EC2 instances.

### 6. Deploy Resources

- Validate Terraform configurations with `terraform validate`.
- Preview changes with `terraform plan`.
- Apply changes using `terraform apply` to create the resources.

### 7. S3 Bucket Setup

- Create an S3 bucket and configure it for public read access if needed.
- Ensure the bucket policy allows necessary permissions.

### 8. Launch EC2 Instances

- Define EC2 instances with the appropriate AMI, instance type, security group, and subnet.
- Use a user data script to configure instances at launch.

### 9. Access Verification

- Obtain the public IP addresses of the EC2 instances and verify they are running correctly by accessing them via a browser.

### 10. Configure Load Balancer

- Create an Application Load Balancer (ALB) and associate it with the subnets.
- Define target groups and health checks for managing traffic distribution.
- Set up ALB listeners to route traffic to your EC2 instances.

### 11. Outputs

- Add output variables in Terraform to display essential information such as load balancer DNS and database endpoint.

### 12. Validate and Apply

- Run `terraform plan` to review the deployment changes.
- Apply the changes with `terraform apply` to finalize the setup.

## 🚧 Challenges Faced

1. **CIDR Block Conflict**: Ensure unique CIDR blocks for each subnet to avoid conflicts.
2. **S3 Bucket Permissions**: Configure public read access to the S3 bucket to prevent unauthorized access errors.

## 📝 Final Notes

Double-check all configurations and permissions to prevent access issues. Following these steps will help you successfully deploy a highly available and scalable application on AWS using Terraform.
