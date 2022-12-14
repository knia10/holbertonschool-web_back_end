# 0x08. User authentication service
<img src="https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/_images/flask-sqlalchemy-title.png" width = 600px length = 300px >
In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Learning Objectivesπ
- π° How to declare API routes in a Flask app
- π° How to get and set cookies
- π° How to retrieve request form data
- π° How to return various HTTP status codes

## Requirements
### General
- π© Allowed editors: `vi`, `vim`, `emacs`
- π© All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- π© All your files should end with a new line
- π© The first line of all your files should be exactly `#!/usr/bin/env python3`
- π© A `README.md` file, at the root of the folder of the project, is mandatory
- π© Your code should use the `pycodestyle` style (version 2.5.x)
- π© You should use `SQLAlchemy` 1.3.x
- π© The length of your files will be tested using `wc`
- π© All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- π© All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- π© A documentation is not a simple word, itβs a real sentence explaining whatβs the purpose of the module, class or method (the length of it will be verified)
- π© All your functions should be type annotated
- π© The flask app should only interact with `Auth` and never with `DB` directly.
- π© Only public methods of `Auth` and `DB` should be used outside these classes.

## Setup
You will need to install `bcrypt`
```
pip3 install bcrypt
```

By **Estefania Ruiz** π¦ From **Holberton School** πͺ