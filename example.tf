provider "aws" {
  profile = "default"
  region  = "us-east-1"
}
resource "aws_instance" "example" {
  ami           = "ami-02396cdd13e9a1257"
  instance_type = "t2.micro"
}