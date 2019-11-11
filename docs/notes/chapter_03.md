# Web-Forms
## Introduction to Flask-WTF

- To handle the web forms in this application I'm going to use the Flask-WTF extension, which is a thin wrapper around the WTForms package that nicely integrates it with Flask. Extensions are a very important part of the Flask ecosystem, as they provide solutions to problems that Flask is intentionally not opinionated about.

- To install Flask-WTF in your virtual environment run:
`(venv) $ pip install flask-wtf`
        
- For any applications except the simplest ones, Flask (and possibly also the Flask extensions that you use) offer some amount of freedom in how to do things, and you need to make some decisions, which you pass to the framework as a list of configuration variables. There are several formats for the application to specify configuration options. The most basic solution is to define your variables as keys using `app.config` in `app.__init__.py`, which uses a dictionary style to work with variables. For example, you could do something like this:
`app = Flask(__name__)`
`app.config['SECRET_KEY'] = 'you-will-never-guess'`
`\# ... add more variables here as needed`
                    
    - While the above syntax is sufficient to create configuration options for Flask, I like to enforce *the principle of separation of concerns*, so instead of putting my configuration in the same place where I create my application I will use a slightly more elaborate structure that allows me to keep my configuration in a separate file that can be used to set the configuration from outside of the application itself.

    - A very extensible format is to use a class to store configuration variables. To keep things nicely organized, create the configuration class in a separate Python module `config.py` in the top-level directory. config.py: (Secret key configuration):
    ```
    import os
    class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ```
                    
    - The configuration settings are defined as class variables inside the Config class. As the application needs more configuration items, they can be added to this class, and later if you find that you need more than one configuration set, you can create subclasses of it. 

    - The `SECRET_KEY` configuration variable is an important part in most Flask applications. Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF (pronounced "seasurf"). The secret key is supposed to be secret, as the strength of the tokens and signatures generated with it depends on no person outside of the trusted maintainers of the application knowing it.

    - The value of the secret key is set as an expression with two terms, joined by the *or* operator. The first term looks for the value of an environment variable, also called SECRET_KEY. The second term, is just a hardcoded string. This is a pattern that you will see me repeat often for configuration variables. The idea is that a value sourced from an environment variable is preferred, but if the environment does not define the variable, then the hardcoded string is used instead. When you are developing this application, the security requirements are low, so you can just ignore this setting and let the hardcoded string be used. But when this application is deployed on a production server, I will be setting a unique and difficult to guess value in the environment, so that the server has a secure key that nobody else knows.

- Now that I have a config file, I need to tell Flask to read it and apply it. That can be done right after the Flask application instance is created using the `app.config.from_object()` method. `app/__init__.py` (Flask configuration):
    ```
    from flask import Flask
    from config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    from app import routes
    ```                    
    The lowercase `config` is the name of the Python module `config.py`, and `Config` is the class defined in this module.

    - Using the Python interpreter where I check what is the value of the secret key:
        ```>>> from microblog import app
        >>> app.config['SECRET_KEY']
        'you-will-never-guess'
        export SECRET_KEY=foo
        >>> from microblog import app
        >>> app.config['SECRET_KEY']
        'foo'
        ```              
          

