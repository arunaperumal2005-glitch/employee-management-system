# Employee Management System

A Django-based web application for managing employee and department information efficiently.

## Overview

The Employee Management System allows organizations to maintain employee records, manage departments, and store employee-related information such as contact details, position, salary, and joining date.

This project was developed using Python and Django to gain practical experience in database management, model relationships, and CRUD operations.

## Features

* Add Employee Records
* Update Employee Information
* Delete Employee Records
* Manage Departments
* Store Employee Contact Details
* Track Employee Positions
* Manage Salary Information
* Store Employee Joining Dates
* Database Integration Using Django ORM

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS

## Database Structure

### Department

| Field       | Type      |
| ----------- | --------- |
| Name        | CharField |
| Description | TextField |

### Employee

| Field       | Type         |
| ----------- | ------------ |
| Name        | CharField    |
| Email       | EmailField   |
| Phone       | CharField    |
| Department  | ForeignKey   |
| Position    | CharField    |
| Salary      | DecimalField |
| Date Joined | DateField    |

## Key Concepts Implemented

* Django Models
* Foreign Key Relationships
* CRUD Operations
* Django ORM
* Database Design
* Form Handling

## Screenshots

### department_details

### employee_details


## Learning Outcomes

* Building Database Relationships
* Managing Employee Data
* Working with Django Models
* Implementing CRUD Functionality
* Database Integration and Management

## Future Enhancements

* Employee Search Functionality
* Authentication and Authorization
* Attendance Management
* Payroll Management
* Dashboard and Reports

## Author

Aruna P

B.Tech Information Technology Graduate

Aspiring Python Full Stack Developer
