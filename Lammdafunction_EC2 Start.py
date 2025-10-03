import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    instance_ids = ['i-0877211f471fe6c14', 'i-0ac221b77927a2c59']
    topic_arn = 'arn:aws:sns:us-east-1:688567266155:MYSNS'
    
    try:
        ec2.start_instances(InstanceIds=instance_ids)
        message = f"✅ EC2 Instances started: {instance_ids}"
        sns.publish(
            TopicArn=topic_arn,
            Subject='EC2 Start Notification',
            Message=message
        )
        return {"status": "success", "message": message}
    except Exception as e:
        error_message = f"❌ Failed to start instances: {str(e)}"
        sns.publish(
            TopicArn=topic_arn,
            Subject='EC2 Start Error',
            Message=error_message
        )
        raise
