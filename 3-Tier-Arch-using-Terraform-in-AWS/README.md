Prerequisites

1. AWS account with IAM user with properly configured user access to AWS
2. Terraform installation
3. EC2 instance key


EXECution:

1. Initialise the TF directory
terraform init
2. Ensure the terraform code is formatted and validated
terraform fmt && terraform validate
3. tfsec - vulnerability check
tfsec
4. Create an execution plan
terraform plan
5. Execute terraform configuration
terraform apply --auto-approve