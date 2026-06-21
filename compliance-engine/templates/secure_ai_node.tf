# Article 11: Technical Documentation (Architectural Proof)
# This configuration enforces strict data isolation and encryption at the infrastructure level.

resource "aws_instance" "ai_processing_node" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  # Enforce root disk encryption for Article 10/11 Data Security
  root_block_device {
    encrypted   = true
    volume_type = "gp3"
  }

  # Enforce IMDSv2 to prevent SSRF and lateral movement
  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required" 
  }

  tags = {
    Name            = "EU-AI-Act-Compliant-Node"
    ComplianceLevel = "High-Risk-Art-11"
  }
}
