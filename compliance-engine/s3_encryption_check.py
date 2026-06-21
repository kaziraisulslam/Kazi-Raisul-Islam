import boto3
import json

def check_s3_encryption():
    """
    Checks if S3 buckets have server-side encryption enabled.
    Maps to EU AI Act Article 10 (Data Governance & Security).
    """
    s3 = boto3.client('s3')
    report = {"status": "success", "non_compliant_buckets": []}
    
    try:
        buckets = s3.list_buckets()['Buckets']
        for bucket in buckets:
            name = bucket['Name']
            try:
                s3.get_bucket_encryption(Bucket=name)
            except:
                report["non_compliant_buckets"].append(name)
        
        return report
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    print(json.dumps(check_s3_encryption(), indent=4))
