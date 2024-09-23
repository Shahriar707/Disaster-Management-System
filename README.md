This is a Disaster Management System web application, a software task provided by Sincos Automation Technologies Ltd.

This is built with Django in backend, HTML and CSS in frontend and SQlite3 as Database. Ensure you have Python 3.8 and Django 4 or higher, you can either manually install them within the virtual environment or using the requirement.txt 

To run this project locally, first download it manually or use the following command:

1. git clone https://github.com/Shahriar707/Disaster-Management-System.git

after downloading the command use another command to enter into the project directory: 

1. cd Disaster-Management-System

Now you have to create a python virtual environment before running it. If your are using Windows then follow the commands below:

1. virtualenv env
2. env\Scripts\activate

or 

1. python -m venv venv
2. venv\Scripts\activate

If you are using macOS or Linux then use the below commands:

1. python3 -m venv venv
2. source venv/bin/activate

after activating the python virtual environment, comeback to the root directory, install Django using: pip install django 

after then change the directory and run following commands in the terminal:

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py collectstatic
4. python manage.py runserver

To create a admin account or superuser, use the below command:?

1. python manage.py createsuperuser

Thank you!
