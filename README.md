# Detecting face and sending Mail, whatsapp message & launching ec2 instance using Terraform

## Changes to do before running the code:

* Update `phone number` in `sendWhatsApp.py` file.
* Update mail-id (sender and receiver) and password in the FaceRecognition.ipynb file where `sendemail.sendemail ` is used.

## Run code

*** `configure AWS` in CMD to configure AWS to Launch the ec2 instance using the Terraform 

## Run

### First
```bash
Face_Recognition_model_creation.ipynb
```

#### This will Train and Save model.

### Second
```bash
Face_Recognition.ipynb
```

#### This will recognize face and run respective functions stored in the below files.

* AWS.tf
* sendemail.py
* sendWhatsApp.py

## Youtube Video Link: https://youtu.be/iNnq8lYN7lY
