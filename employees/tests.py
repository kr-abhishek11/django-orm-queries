from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee, Project


class EmployeeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(project_name='Project 1', description='Project Description', start_date='2022-05-10', end_date='2022-06-10')
        self.employee_data = {'first_name': 'Kumar', 'last_name': 'Abhishek', 'email': 'kumar.abhishek@infobeans.com', 'department': 'IT', 'project': self.project}
        self.employee = Employee.objects.create(**self.employee_data)

    def test_get_all_employees(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        response = self.client.post('/employees/', self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee_detail(self):
        response = self.client.get(f'/employees/{self.employee.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        updated_data = {'first_name': 'Kumar', 'last_name': 'Abhishek', 'email': 'kumar.abhishek@infobeans.com', 'department': 'Services'}
        response = self.client.put(f'/employees/{self.employee.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(f'/employees/{self.employee.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProjectAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project_data = {'project_name': 'Pidilite', 'description': 'Loyalty revamp app', 'start_date': '2024-05-09', 'end_date': '2024-08-10'}
        self.project = Project.objects.create(**self.project_data)

    def test_get_all_projects(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        response = self.client.post('/projects/', self.project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_project_detail(self):
        response = self.client.get(f'/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        updated_data = {'project_name': 'Pidilite', 'description': 'Updated Description', 'start_date': '2024-05-09', 'end_date': '2024-08-10'}
        response = self.client.put(f'/projects/{self.project.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        response = self.client.delete(f'/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

   
