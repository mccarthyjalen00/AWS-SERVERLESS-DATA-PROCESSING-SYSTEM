import boto3

ec2 = boto3.resource('ec2')

def deploy_instance():
    # Launches a new EC2 instance automatically
    instances = ec2.create_instances(
        ImageId='ami-xxxxxxxxxxxxxxxxx', # Replace with a valid Linux AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='my-key-pair'
    )
    print(f"Deployed Instance: {instances[0].id}")

def monitor_instances():
    # Monitors existing instances and prints their status
    for instance in ec2.instances.all():
        print(f"ID: {instance.id}, State: {instance.state['Name']}")

if __name__ == "__main__":
    deploy_instance()
    monitor_instances()
