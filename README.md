# 🚀 Automate EC2 Start/Stop Using AWS Lambda, EventBridge & SNS


👨‍💻 Author

Your Name: YallaReddy Gundladurthi
 AWS Cloud / DevOps Engineer
🔗 LinkedIn : https://www.linkedin.com/in/yallareddy-g-4a1aa617a/

🐱 GitHub : https://github.com/gyallareddy

This project provides a **serverless solution** to automatically start and stop EC2 instances on a **daily schedule**, using **AWS-native services** — no cron servers or scripts required!

---

## 📌 Use Case

Start and stop selected EC2 instances during working hours to:
- ⏱ Save time and manual effort
- 💰 Reduce AWS costs by stopping idle resources
- 📩 Receive email notifications on every start/stop action

---

## 🕒 Schedule

- ✅ Start EC2 instances at **9:00 AM IST** (`03:30 UTC`)
- 🛑 Stop EC2 instances at **6:00 PM IST** (`12:30 UTC`)
- 📅 Runs **Monday through Friday** only

---

## 🧰 AWS Services Used

| Service            | Purpose                                |
|--------------------|-----------------------------------------|
| AWS Lambda         | Serverless function to start/stop EC2   |
| Amazon EventBridge | Schedule Lambda triggers (cron-based)   |
| Amazon EC2         | Target instances to manage              |
| Amazon SNS         | Email notifications on actions          |
| IAM                | Permissions for Lambda execution        |

---

## 🛠️ Setup Guide

### 1. 🔔 Create SNS Topic

- Go to **Amazon SNS > Topics > Create topic**
- Choose `Standard`
- Name: `MYSNS`
- Add an **email subscription**
- Confirm the email from your inbox

---

### 2. 🔐 Create IAM Role for Lambda

Attach this policy to your Lambda's IAM role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:us-east-1:688567266155:MYSNS"
    }
  ]
}


### 3. 🔐 Create Lambda Functions For Start and STOP and event Formats in JSON

For START FUNCTION Refer files in REPO
Lammdafunction_EC2 Start.py
Start EC2 Instances – Event JSON

FOR STOP function Refer files in REPO
Lambdafunction_EC2stop.py
Stop EC2 Instances – Event JSON

Step 4: Create EventBridge Rules

⏰ Remember: AWS EventBridge uses UTC, so you'll convert IST to UTC:

09:00 AM IST = 03:30 AM UTC

06:00 PM IST = 12:30 PM UTC

⏲️ Rule 1 – Start Instances

Go to Amazon EventBridge > Rules > Create Rule

Create two EventBridge rules:
⏲️ Rule 1 – Start Instances
🟢 Start EC2

Time (UTC): 03:30 AM
Cron Expression: cron(30 3 ? * 2-6 *)
Target: start_ec2_instances Lambda
⏲️ Rule 2 – Stop Instances
🔴 Stop EC2
Time (UTC): 12:30 PM
Cron Expression: cron(30 12 ? * 2-6 *)
Target: stop_ec2_instances Lambda

4. 📅 EventBridge Schedule (Trigger)

Create two EventBridge rules:

🟢 Start EC2

Time (UTC): 03:30 AM
Cron Expression: cron(30 3 ? * 2-6 *)
Target: start_ec2_instances Lambda

🔴 Stop EC2
Time (UTC): 12:30 PM
Cron Expression: cron(30 12 ? * 2-6 *)
Target: stop_ec2_instances Lambda

🏷️ Tags

aws lambda ec2 eventbridge sns serverless automation cloud devops python cost-optimization




