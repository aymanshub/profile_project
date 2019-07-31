# User Profile with Django

Step to get the project running.

1. Use the `requirements.txt` file to install the project dependencies.

2. Run your migrations to create the tables in the database.
   `python manage.py migrate`

3. Run the server.
   `python manage.py runserver`


Once you add a Model with some fields or each time you make changes to the Model, make sure you run:

`python manage.py makemigrations` to create an initial/new migration file inside the `migrations` folder for that `<app>`. So when you run the `migrate` command it knows how to setup or alter the database tables before data starts getting put in those tables.

**Prerequisites:**
1. Local windows machine
2. Python 3.6

**Built With:**
1. Django - a Python-based free and open-source web framework.

**Authors:**

[Ayman Said](https://www.linkedin.com/in/ayman-said-96819726) 