import boto3

def verify_instance_compliance(instance_id):
    ec2 = boto3.client('ec2')
    instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
    
    # Check for IMDSv2 requirement
    metadata = instance.get('MetadataOptions', {})
    if metadata.get('HttpTokens') == 'required':
        print(f"[PASS] {instance_id}: IMDSv2 Enforced (Article 11 Compliant)")
    else:
        print(f"[FAIL] {instance_id}: IMDSv2 NOT Enforced")

if __name__ == "__main__":
    # Replace with a real instance ID to test
    verify_instance_compliance('i-0123456789abcdef0')
