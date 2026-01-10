# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## Core Philosophy

- **Don't Repeat Yourself (DRY):** The DRY principle is central to Django. The goal is to minimize redundant code and promote reusable components.
- **Convention over Configuration:** Django provides sensible defaults for many settings, which means you don't have to configure everything from scratch.
- **Batteries-Included:** Django comes with a rich set of features out of the box, including an object-relational mapper (ORM), an admin interface, authentication, and more.

## Key Features

### Object-Relational Mapper (ORM)
Django's ORM allows you to interact with your database, like you would with SQL. In fact, Django’s ORM is a way to write SQL in Python. You define your data models as Python classes, and Django handles the communication with the database.

### Admin Interface
Django provides a ready-to-use, production-ready administrative interface. It's a powerful and time-saving feature that allows trusted users to manage content on your site.

### URL Routing
Django uses a URL dispatcher to route HTTP requests to the appropriate view based on the requested URL. You create a `urls.py` file to map URL patterns (as regular expressions) to your view functions or classes.

### Template Engine
Django's template engine allows you to separate the design of your web pages from the Python code. You can create HTML templates with special syntax to display dynamic data.

### Forms
Django provides a powerful form-handling library that simplifies the process of creating forms, validating user input, and processing data.

### Authentication and Security
Django comes with a built-in user authentication system. It also provides protection against common security threats like Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and SQL injection.

## Getting Started

1.  **Installation:**
    ```bash
    pip install Django
    ```

2.  **Start a Project:**
    A Django project is a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.
    ```bash
    django-admin startproject myproject
    ```
    This will create a `myproject` directory with the basic project structure.

3.  **Create an App:**
    An application is a web application that does something – e.g., a weblog system, a database of public records or a simple poll app. A project can contain multiple apps.
    ```bash
    cd myproject
    python manage.py startapp myapp
    ```

4.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    This starts a lightweight development web server on your local machine.

## Project vs. App

-   A **Project** can contain multiple **Apps**. A project handles the overall configuration.
-   An **App** is a self-contained module that handles a specific feature of your website (e.g., a blog, a user authentication system). Apps are designed to be reusable across different projects.
