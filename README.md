# AWS User Registration Coursework App

A Flask and SQLite web application deployed to an Ubuntu 24.04 EC2 instance for Introduction to Cloud Computing Project 2.

## Live deployment

- Public URL: http://3.89.79.132/
- Platform: AWS EC2, Ubuntu Server 24.04 LTS, Apache2, mod_wsgi, Flask, SQLite3

## Assignment features

- User registration: username, password, first name, last name, email, and address
- SQLite-backed user storage
- Profile page displaying the submitted user details
- Re-login form that retrieves a saved user profile
- Text-file upload and server-side storage
- Word-count display for the uploaded file
- Download link for the uploaded file

## Project files

- `app.py`: Flask application and SQLite data model
- `user-data.sh`: EC2 user-data provisioning script

## Deployment summary

1. Launch Ubuntu Server 24.04 LTS on EC2.
2. Allow inbound HTTP (TCP port 80) in the instance security group.
3. Install Apache2, `libapache2-mod-wsgi-py3`, Python Flask, and SQLite3.
4. Place `app.py` and `awsapp.wsgi` in `/var/www/awsapp/`.
5. Enable the Apache virtual-host configuration and restart Apache.

## Local verification

The deployed app was verified from outside the EC2 instance with:

- HTTP 200 response from the public address
- Registration POST redirecting to a rendered profile page
- Uploaded file word count and download link
