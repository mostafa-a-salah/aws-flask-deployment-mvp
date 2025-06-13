terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "app_server" {
  ami           = "ami-020cba7c55df1f615" # Ubuntu 24.04 LTS in us-east-1
  instance_type = "t2.micro"             # Free Tier eligible

  tags = {
    Name = "MyWebAppServer-Terraform"
  }
}
