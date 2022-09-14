# PBP Assignment 2: Introduction to Django and Models View Template (MVT) Concept

[Project Template](https://github.com/pbp-fasilkom-ui/assignment-repository)<br/>
[Heroku Application](https://raaassignment2.herokuapp.com/katalog/)

## Django diagram

![Django Diagram](https://krify.co/wp-content/uploads/2019/06/Django-Work-flow.jpg)
<sub>taken from the [PBD 22 repository](https://pbp-fasilkom-ui.github.io/ganjil-2023/en/assignments/tutorial/tutorial-1)</sub>

From the diagram, when a user request to Django, firstly it will be processed through **urls.py** then to **views.py**. If there exist a database, then **views.py** will take all of the query(in json file) to **models.py**. The result will be mapped into **katalog.html** before the user gets **katalog.html** as the response.

## Virtual environment

It is not mandatory to use python's virtual environment (venv) module. But it is best practice to use it. A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments. Thus, isolating the project as to not be tangled with other existing projects.


## Way to implement things

#### Create a function on views.py that can do querying into models and returns the data into a HTML.

> Import the item from class models. Then, create a function that take the item and some other variables as context. That return them along with the defined HTML file using the render function from django's module.

#### Create a routing to map the function that you've created in views.py.

> On **urls.py** use the function from **views.py** for routing the context to the defined HTML file.

#### Map the data that has been returned into HTML by using Django syntax for templates and data mapping.

> Use the for loop to iterate all the items from the database. And present it via table.

#### Deploy your assignment into Heroku so that your friends and your teaching assistants can access it via the Internet.

> Make the application on Heroku and conect it with the repository. Then make repository secret with the appropriate application name and API. Now it can be [accessed](https://raaassignment2.herokuapp.com/katalog/).