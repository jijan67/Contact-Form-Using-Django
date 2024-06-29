Running a Django project in Visual Studio Code (VS Code) involves setting up your development environment, creating and managing a virtual environment, and running your Django server. Below are the detailed steps to do this.

Step 1: Open Your Project in VS Code
Open VS Code
Open Visual Studio Code.

Open Your Project Folder

Click on File -> Open Folder.
Select your Django project folder (contact_list_project).
Step 2: Set Up a Virtual Environment
Open Terminal in VS Code

Go to View -> Terminal to open a new terminal window within VS Code.
Create a Virtual Environment

bash
Copy code
python -m venv venv
Activate the Virtual Environment

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install Django
If you haven't installed Django yet, run:

bash
Copy code
pip install django
Step 3: Create Superuser (If Not Done Yet)
Run createsuperuser Command

bash
Copy code
python manage.py createsuperuser
Follow the Prompts

Enter the username, email address, and password as prompted.
Step 4: Run the Django Server
Run the Server

bash
Copy code
python manage.py runserver
Access the Application

Open your web browser and navigate to http://127.0.0.1:8000/ to view the contact list.
Navigate to http://127.0.0.1:8000/sign-up/ to view the sign-up form.
Navigate to http://127.0.0.1:8000/admin/ to access the admin interface.
Step 5: Create and Edit Files
Create and Edit Files in VS Code
Use the file explorer in VS Code to create and edit your Django app files, such as models.py, views.py, forms.py, urls.py, and templates.
Step 6: Additional VS Code Extensions (Optional)
Install Django and Python Extensions
Go to the Extensions view in VS Code (Ctrl+Shift+X or Cmd+Shift+X on macOS).
Search for and install the following extensions:
Python by Microsoft (essential for Python development)
Django by thecodepath (optional, but provides useful features for Django development)
Example Structure in VS Code
Your project structure should look something like this in the VS Code explorer:

markdown
Copy code
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
