* Use python to create a virtual environment named venv
python -m venv venv

* Activate the virtual environment venv
- source venv/bin/activate

* deactivate virtual environment
- deactivate

* Install Flask in the virtual environment
- pip install flask

* In Python, a sub-directory that includes a __init__.py file is considered a package, and can be imported. When you import a package, the __init__.py executes and defines what symbols the package exposes to the outside world.

* The __name__ variable from Python provides the name of the package.
    - In the instance `app=Flask(__name__) flask uses this value to find the location this package on disk so it can find other files at the same location.
    - The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used, in this case `app`. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files, which I will cover in Chapter 2. For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way.

* So what goes in the routes module? The routes are the different URLs that the application implements. In Flask, handlers for the application routes are written as Python functions, called view functions. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.

* A common pattern with decorators is to use them to register functions as callbacks for certain events. In this case, the @app.route decorator creates an association between the URL given as an argument to route() and the function which it decorates. In this example there are two decorators, which associate the URLs / and /index to this function. This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response. 

* To tell flask where the application is located we need to create an environmental variable  called FLASK_APP to point to the module that defines the application. We don't need to give flask the name of the application because flask will look for a variable called `app`

* Run application
- flask run
