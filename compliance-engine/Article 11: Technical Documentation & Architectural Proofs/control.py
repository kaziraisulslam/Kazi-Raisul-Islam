# compliance-engine/EU-AI-Act/Art-11-Technical-Documentation/control.py
import boto3
import json

def verify_architecture_compliance(region="eu-central-1"):
    """Validates that infrastructure matches Art 11 security specs."""
    ec2 = boto3.client('ec2', region_name=region)
    
    # Audit for required encryption on all volumes
    volumes = ec2.describe_volumes()
    violations = []
    
    for vol in volumes['Volumes']:
        if not vol.get('Encrypted'):
            violations.append(vol['VolumeId'])
            
    artifact = {
        "article": "EU-AI-Act-Art-11",
        "status": "NON-COMPLIANT" if violations else "COMPLIANT",
        "unencrypted_volumes": violations,
        "region": region
    }
    
    with open('compliance-engine/EU-AI-Act/Art-11-Technical-Documentation/artifact.json', 'w') as f:
        json.dump(artifact, f, indent=4)
    return artifact

if __name__ == "__main__":
    print(verify_architecture_compliance())
