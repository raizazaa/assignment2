# PBP Assignment 4: mplementing Forms and Authentication Using Django

[Heroku Application](https://raaassignment2.herokuapp.com/todolist/)

## What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?
It is a way to protect from CSRF attacks. It ensures the GET requests are side effect free. Requests via ‘unsafe’ methods, such as POST, PUT, and DELETE, can then be protected by Django's CSRF protection.
Without CSRF protection, the program will be exposed to CSRF attack that can take login informations.

## Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
Yes we can. If we generate it automaticly, it uses python's syntax to generate the form. While if we create it manually, the code (such as the required fields) is present in the HTML file instead of forms file.

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
Once user submit the new task, it will be handled by the create_task function in views. Where it will call TaskForm from forms.py and it save form data as the database. Then it will be return to the HTML todolist template.

## Way to implement things
Create django project by the function startapp todolist and then set path and installed apps in the django_app folder. Then create the data models accordingly. I implement the register, login, and logout forms by making the appropriate function in views, and then return it to the HTML files. I then create the todolist.html and add the username, buttons, and the tables. To create the form, I used class modelForm and have the fields required. Then I route the functions from views to their HTMLs. I used my assignment2 Heroku app deployment. Lastly, I made two accounts with three task by registering it and adding new task.