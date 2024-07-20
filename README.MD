
# 🌟 Terraform Three-Tier Architecture Project

## 📋 Prerequisites

Before you start, ensure you have:

- **AWS Account**: An IAM user with permissions for S3, EC2, VPC, Load Balancer, and Admin access.
- **VS Code**: If you don’t have it installed, you can use GitHub Codespaces.
- **Terraform**: Installed for infrastructure management.

## 🛠️ Project Overview

This project implements a **Three-Tier Architecture** to enhance scalability, availability, and security. The architecture separates the application into three layers:

1. **Web Tier**: Handles HTTP requests and serves the frontend.
2. **Application Tier**: Processes business logic and application functionalities.
3. **Data Storage Tier**: Manages data persistence and retrieval.

By distributing resources across multiple Availability Zones, the application maintains high availability and auto-scaling capabilities, ensuring continuous operation even if one zone fails.

## 🚀 Getting Started

### 1. Set Up IAM User

Create an IAM user with the following permissions:
- **S3**
- **EC2**
- **VPC**
- **Load Balancer**
- **Admin**

### 2. Configure Development Environment

- **VS Code**: Use GitHub Codespaces if you don’t have VS Code installed locally. Search for the Dev Configuration file and activate the environment.
- **Terraform**: Configure Terraform in your Codespaces by adding the necessary `tf` files and setting up AWS credentials.

### 3. AWS Configuration

- **Access Keys**: Go to AWS Security Credentials, create an access key, and configure AWS in Codespaces using `aws configure`. Enter your Access Key, Secret Key, region, and format.

### 4. Initialize Terraform

- Create a project folder and set up the Terraform provider for AWS.
- Run `terraform init` to check if Terraform is connected to AWS properly.

### 5. Define Infrastructure

- **VPC**: Create a Virtual Private Cloud (VPC) with CIDR block.
- **Subnets**: Define two subnets across different Availability Zones.
- **Internet Gateway**: Attach to the VPC for internet access.
- **Route Table**: Define routing rules and associate with subnets.
- **Security Groups**: Configure inbound and outbound rules for EC2 instances.

### 6. Deploy Resources

- Validate Terraform configurations with `terraform validate`.
- Preview changes with `terraform plan`.
- Apply changes using `terraform apply` to create resources.

### 7. S3 Bucket Setup

- Create an S3 bucket and configure it for public read access if required.
- Ensure that the bucket policy allows necessary permissions.

### 8. Launch EC2 Instances

- Define EC2 instances with the appropriate AMI, instance type, security group, and subnet.
- Use the user data script to configure instances on launch.

### 9. Access Verification

- Copy the public IP addresses of EC2 instances and paste them into your browser to verify if they are running correctly.

### 10. Configure Load Balancer

- Create an Application Load Balancer (ALB) and associate it with subnets.
- Define target groups and health checks to manage traffic distribution.
- Set up ALB listeners to route traffic to your EC2 instances.

### 11. Outputs

- Add output variables to display essential information on the terminal.

### 12. Validate and Apply

- Run `terraform plan` and `terraform apply` to finalize the deployment.

## 🚧 Challenges Faced

1. **CIDR Block Conflict**: Assigned the same CIDR block to both subnets. Ensure unique CIDR blocks for each subnet.
2. **S3 Bucket Permissions**: Forgot to grant public read access to the S3 bucket, resulting in unauthorized access errors.

## 📝 Final Notes

Ensure all configurations are correct and permissions are set appropriately to avoid access issues. By following these steps, you’ll successfully deploy a highly available and scalable three-tier architecture on AWS using Terraform.

