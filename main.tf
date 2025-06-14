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
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  tags = {
    Name = "MyWebAppServer-Terraform"
  }
}
resource "aws_security_group" "app_sg" {
  name        = "webapp-sg"
  description = "Allow SSH and HTTP inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
