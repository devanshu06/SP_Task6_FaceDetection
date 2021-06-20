import os

def ec2_and_ebs():
    os.system("terraform init")
    os.system("terraform apply -auto-approve")