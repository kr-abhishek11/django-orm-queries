Django ORM Queries for Employee and Project Models
This repository contains sample Django ORM queries for the Employee and Project models. These queries demonstrate how to interact with the database using Django's powerful ORM (Object-Relational Mapping) system.

Getting Started
To run these queries, make sure you have Django installed in your Python environment. If not, you can install it using pip:

 - pip install django

Clone this repository to your local machine:
- git clone <repository-url>
- cd <repository-directory>

Project Model:
The Project model represents a project within an organization. It has the following fields:

project_name: A character field representing the name of the project. It has a maximum length of 100 characters.
description: A text field providing a detailed description of the project.
start_date: A date field indicating the start date of the project.
end_date: A date field indicating the end date of the project.
Projects are identified by their unique project names, and each project may have a different duration from start to end.

Employee Model:
The Employee model represents an individual employee within the organization. It has the following fields:

first_name: A character field representing the first name of the employee. It has a maximum length of 100 characters.
last_name: A character field representing the last name of the employee. It has a maximum length of 100 characters.
email: An email field representing the email address of the employee. It is unique across all employees.
department: A character field indicating the department in which the employee works. It has a maximum length of 100 characters.
project: A foreign key relationship with the Project model, indicating the project to which the employee is assigned. It establishes a one-to-many relationship, as each employee may be associated with one project, while each project may have multiple employees.
Employees are uniquely identified by their email addresses, and each employee is associated with a specific department and project within the organization.

These models provide a structured way to represent projects and employees in a Django application, allowing for efficient management and organization of data within the system.

- First of all you will need to migrate all the django models. Use the following commands for the same
    python manage.py makemigrations
    python manage.py migrate

- Register your apps in admin.py in order to add data via the admin panel of django (admin/)

- Create a superuser in order to access the admin panel
    python manage.py createsuperuser (provide credentials for the same)

- Run the development server using - python manage.py runserver
- Add the data into the models in order to run the below ORM queries


ORM Queries
Django ORM Queries for Project Model:
- Get all projects:
    projects = Project.objects.all()
- Filter projects by project name:
    projects = Project.objects.filter(project_name='Project Name')
- Get projects with start date after a specific date:
    projects = Project.objects.filter(start_date__gt='2022-01-01')
- Get projects with end date before a specific date:
    projects = Project.objects.filter(end_date__lt='2023-01-01')
- Get projects ordered by start date in descending order:
    projects = Project.objects.order_by('-start_date')
- Get the first project ordered by project name:
    project = Project.objects.order_by('project_name').first()

Django ORM Queries for Employee Model:
- Get all employees:
    employees = Employee.objects.all()
- Filter employees by department:
    employees = Employee.objects.filter(department='IT')
- Get employees with a specific email:
    employees = Employee.objects.filter(email='example@example.com')
- Get employees associated with a project (using reverse relation):
    project = Project.objects.get(project_name='Project Name')
    employees = project.employees_projects.all()
- Get employees ordered by last name:
    employees = Employee.objects.order_by('last_name')
- Count the number of employees in a department:
    count = Employee.objects.filter(department='HR').count()