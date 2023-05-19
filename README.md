# Create Task Manager Using Flask

This is a guide on how to create a Task Manager web application using Flask, a Python web framework. The Task Manager allows users to add, edit, and delete tasks with a title and description.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python (version 3.6 or later)
- Flask (install using `pip install flask`)

## Project Setup

1. Create a new directory for your project and navigate to it.
2. Initialize a new virtual environment:
   ```shell
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```shell
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```shell
     source venv/bin/activate
     ```
4. Create a new Python file called `app.py` for our Flask application.

## Setting Up the Flask Application

1. Open `app.py` and import the necessary modules:
   ```python
   from flask import Flask, render_template, request, redirect, url_for
   from datetime import datetime
   ```
2. Create an instance of the Flask application:
   ```python
   app = Flask(__name__)
   ```
3. Define a route for the home page:
   ```python
   @app.route('/')
   def index():
       return render_template('index.html')
   ```
4. Add a route to handle the form submission for adding a new task:
   ```python
   @app.route('/add', methods=['POST'])
   def add_task():
       title = request.form['title']
       desc = request.form['desc']
       date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       # TODO: Save the task to a database or any other storage
       return redirect(url_for('index'))
   ```
5. Add a route to render the form for adding a new task:
   ```python
   @app.route('/add')
   def show_add_form():
       return render_template('add.html')
   ```
6. Add a route to handle the form submission for editing a task:
   ```python
   @app.route('/edit/<int:task_id>', methods=['POST'])
   def edit_task(task_id):
       title = request.form['title']
       desc = request.form['desc']
       # TODO: Update the task with the given task_id in the database or storage
       return redirect(url_for('index'))
   ```
7. Add a route to render the form for editing a task:
   ```python
   @app.route('/edit/<int:task_id>')
   def show_edit_form(task_id):
       # TODO: Retrieve the task with the given task_id from the database or storage
       # Pass the task data to the template
       return render_template('edit.html', task=task)
   ```
8. Add a route to handle deleting a task:
   ```python
   @app.route('/delete/<int:task_id>')
   def delete_task(task_id):
       # TODO: Delete the task with the given task_id from the database or storage
       return redirect(url_for('index'))
   ```
9. Run the Flask application:
   ```shell
   flask run
   ```

## HTML Templates

Create the following HTML templates in a new directory called `templates`:

1. `index.html`:
   ```html
   {% extends "base.html" %}

   {% block main %}
     <!-- Display the tasks here -->
   {% endblock %}
   ```

2. `add.html`:
   ```html
   {% extends "base.html" %}

   {% block main %}
     <h2>Add Task

</h2>
     <form action="{{ url_for('add_task') }}" method="POST">
       <label for="title">Title:</label>
       <input type="text" id="title" name="title" required><br><br>
       <label for="desc">Description:</label>
       <textarea id="desc" name="desc" required></textarea><br><br>
       <input type="submit" value="Add Task">
     </form>
   {% endblock %}
   ```

3. `edit.html`:
   ```html
   {% extends "base.html" %}

   {% block main %}
     <h2>Edit Task</h2>
     <form action="{{ url_for('edit_task', task_id=task.id) }}" method="POST">
       <label for="title">Title:</label>
       <input type="text" id="title" name="title" value="{{ task.title }}" required><br><br>
       <label for="desc">Description:</label>
       <textarea id="desc" name="desc" required>{{ task.desc }}</textarea><br><br>
       <input type="submit" value="Update Task">
     </form>
   {% endblock %}
   ```

4. `base.html`:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <!-- Required meta tags -->
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

       <!-- Bootstrap CSS -->
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">

       <title>Task Manager</title>
     </head>
     <body>
       <div class="container-fluid">
         <nav class="navbar navbar-expand-lg navbar-light bg-light">
           <ul class="navbar-nav">
             <li class="nav-item"><a href="{{ url_for('index') }}" class="nav-link">Tasks</a></li>
             <li class="nav-item"><a href="{{ url_for('show_add_form') }}" class="nav-link">Add New</a></li>
           </ul>
         </nav>
         <br>
         {% with messages = get_flashed_messages() %}
           {% if messages %}
             {% for message in messages %}
             <div class="alert alert-primary">
               {{ message }}
             </div>
             {% endfor %}
           {% endif %}
         {% endwith %}
         <br>
         <h1>Task Manager</h1>
         <br>
         {% block main %}{% endblock %}
       </div>

       <!-- Additional scripts -->
       <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.0/js/bootstrap.min.js"></script>
     </body>
   </html>
   ```

## Conclusion

Congratulations! You have created a Task Manager web application using Flask. The application allows users to add, edit, and delete tasks. You can further enhance the application by connecting it to a database, implementing authentication, and adding additional features as per your requirements.

Remember to always follow best practices for web development, including validating user input, securing sensitive data, and properly handling errors. Enjoy building more features on top of this foundation!
