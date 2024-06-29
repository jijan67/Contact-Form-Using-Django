Running a Django project in Visual Studio Code (VS Code) involves setting up your development environment, creating and managing a virtual environment, and running your Django server. Below are the detailed steps to do this.

Step 1: Open Your Project in VS Code
Open VS Code
Open Visual Studio Code.
Open Your Project Folder
Click on File -> Open Folder.
Select your Django project folder (contact_list_project).

Step 2: Open Terminal in VS Code
Go to View -> Terminal to open a new terminal window within VS Code.
Run given below code on Terminal:
Code->cd contact_list_project
Install Django
If you haven't installed Django yet, run on Terminal:
Code->pip install Django

Step 3: Run the Django Server
Run the Server following this code on terminal:
Code->python manage.py runserver

Access the Application
Open your web browser and navigate to http://127.0.0.1:8000/ to view the contact list.
Navigate to http://127.0.0.1:8000/sign-up/ to view the sign-up form.
Navigate to http://127.0.0.1:8000/admin/ to access the admin interface.

Your project structure should look something like this in the VS Code explorer:
contact_list_project/
├── contact_list_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── contacts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── contacts/
│   │       ├── contact_list.html
│   │       └── sign_up.html
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── venv/
    ├── bin/ (or Scripts/ on Windows)
    ├── include/
    ├── lib/
    └── ...

By following these steps, you should be able to run your Django project in VS Code smoothly.
