# AWS-SERVERLESS-DATA-PROCESSING-SYSTEM

An automated, event-driven data pipeline built to optimize ingestion workflows and automate cloud infrastructure management. This project demonstrates proficiency in Serverless Architecture, Cloud Automation, and Infrastructure as Code (IaC) using the AWS ecosystem

Project Overview
This system addresses the challenges of manual data handling and server management by implementing an end-to-end serverless workflow. By utilizing AWS Lambda and S3, the system triggers automated processing the moment data is ingested. Additionally, the project includes custom Python/Boto3 scripts to automate EC2 lifecycle management, significantly reducing human error and configuration time.

Technical Features
  1. Event-Driven Ingestion: Leveraged S3 Bucket Events to trigger AWS Lambda functions, resulting in a high-speed,
     automated data ingestion pipeline.
  3. Serverless Compute: Engineered Python-based Lambda functions to process data on-demand, eliminating the need for
     24/7 server maintenance and reducing overhead.
  5. Automated Cloud Ops: Developed automation scripts using the Boto3 SDK to programmatically deploy, monitor, and
     manage EC2 backend services.
  7. Efficiency Optimization: Achieved a 40% reduction in manual configuration by replacing console-based tasks with
     scripted cloud operations.

Project Structure
  1. lambda/: Contains lambda_function.py, the core logic for event-driven data processing.
  2. scripts/: Includes ec2_manager.py for automated deployment and monitoring of EC2 instances.
  3. infrastructure/: Documentation of the IAM policies and S3 trigger configurations used.
  
Motivation:
The goal of this project was to transition from manual, server-reliant workflows to a modern Cloud-Native approach. This allowed me to:
  1. Enhance Speed: Remove the latency of manual data movement through automation.
  2. Scale Dynamically: Ensure the infrastructure could handle variable data loads without manual intervention.
  3. Implement Best Practices: Practice the principle of "Least Privilege" through IAM and "Everything as Code" through
     Python automation.

How to Run
Prerequisites
  1. An active AWS Account.
  2. Python 3.x and the boto3 library.
  3. Configured AWS CLI credentials.

Setup Instructions
  1. Deploy the Lambda: Upload the code from the lambda/ directory to your AWS Lambda function.
  2. Configure S3: Set up an Event Notification on your S3 bucket to trigger the Lambda function for all ObjectCreated
     events.
  4. Run Automation Scripts: Execute the EC2 manager locally to automate instance deployment:
       python scripts/ec2_manager.py
