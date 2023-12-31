terraform {
  required_version = "1.5.2"
    cloud {
        organization = "DevOpsOrg"

        workspaces {
            tags = ["cloud:aws", "security"]
        }
    }
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.7.0"
    }
  }
}

