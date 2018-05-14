# FlaskProductSiteDemo

This is a Flask demo site I've built to improve my knowledge of the framework.  It allows listing of products, management of categories, products and users in an admin panel as well as an administrative access control at the route level.

This project uses the following packages:
```
Flask
Flask-Bcrypt
Flask-Login
Flask-SQLAlchemy
Flask-WTF
```

The Flask packages install their related dependency packages through pip, so pip install will handle those.

To use this, you just need to clone it to a machine with Python 3 installed and the packages listed above setup.

You will need to handle a couple of steps prior to running it.

First you need to setup some configuration values, you can either edit the **productsite.config.py** configuration values, or export values into the system arguments.  Below is what you need to setup:

```
SITE_DB_URI
SITE_SECRET_KEY
```
Use **export** on Linux/Unix/Mac systems or **set** on Windows to setup the parameters. Example:
```
export SITE_DB_URI=sqlite:///site.db
```

Note: On Linux systems, you can add these values to your **.bash_profile** file to make these stick past your current session.

Note: The **SITE_DB_URI** can be set to ```sqlite:///site.db``` to use the default database, or you can configure it to any SQLAlchemy supported database.  Note that you might need to install additional drives to get it up and working with other DB's, this will work out of the box with SQLite3.

Once you have the system arguments or configuration setup as you'd like, you'll need to setup the database structure using the Build.py, this can also be used to build a clean database.
```
python3.6 build.py
```

If using SQLite3, this will create a database in the **productsite** directory called site.db (or what ever you named it).  If not, it will attempt to connect to your database source (e.g MySQL, Mongo, Postgres etc) and setup a database based on your settings.

This will setup the routes and some intial product categoryies, feel free to edit the **build.py** if you want to change the defaults to your liking.

This will setup also an inital administrative user **admin@admin.com** with the pasword **password1**, I know, super secure, but this is also going to be over HTTP, so don't go acting like this is a production ready project.

Once you've run **build.py** you can then run the creatively named **run.py**.
```
python3.6 run.py
```

This will launch the Flask application.  You can edit the **run.py** to disable debug and change the host and pass in any parameters you need to run the application.

I've run into issues with the host when running on a separate (non-local) machine, if you run it under the default, it will run as localhost or 127.0.0.1, which won't be accessible outside the machine.  To fix this, set the host='' parameter to the external facing IP address of your host machine (e.g 192.168.1.100, use ```ip addr show``` Nix or ```ipconfig``` Windows )

After the the application is running you should be able to access to site via a web browser by accessing the IP address via port 5000, unless you've set it differently.

Access the login screen by clicking the login button in the upper right, using the admin login from above.  There you can create a new admin user with your own credentials.  You can now explore the site and break things.
