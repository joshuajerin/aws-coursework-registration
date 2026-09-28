# PROJECT 2: AWS Submission Notes

## Public AWS application URL

http://3.89.79.132/

## Source code and evidence repository

https://github.com/joshuajerin/aws-coursework-registration

## Deployment

- AWS EC2 instance: `i-0a58cdea1886c5215`
- Operating system: Ubuntu Server 24.04 LTS
- Instance type: t3.micro
- Web server: Apache2 with mod_wsgi
- Application: Python Flask
- Database: SQLite3

## Required web application behavior

- Registration form stores username, password, first name, last name, email, and address.
- Profile page displays the stored submitted details.
- Re-login page authenticates a user and loads their profile.
- Text-file upload is stored on the server.
- Profile shows the uploaded file's word count and provides a download link.

## Included evidence files

- `evidence-ec2-security.png`: deployed EC2/security group evidence
- `evidence-live-registration.png`: public registration page
- `evidence-profile-upload.png`: stored profile, uploaded file word count, and download action
