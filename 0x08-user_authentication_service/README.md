# 0x08. User authentication service
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fflask-sqlalchemy.palletsprojects.com%2F&psig=AOvVaw11GPyT1drZLOYm3NrEWBMl&ust=1666215635882000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCOiRqprf6voCFQAAAAAdAAAAABAM" width = 600px length = 300px >
In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Learning Objectives📖
- 🔰 How to declare API routes in a Flask app
- 🔰 How to get and set cookies
- 🔰 How to retrieve request form data
- 🔰 How to return various HTTP status codes

## Requirements
### General
- 🚩 Allowed editors: `vi`, `vim`, `emacs`
- 🚩 All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- 🚩 All your files should end with a new line
- 🚩 The first line of all your files should be exactly `#!/usr/bin/env python3`
- 🚩 A `README.md` file, at the root of the folder of the project, is mandatory
- 🚩 Your code should use the `pycodestyle` style (version 2.5.x)
- 🚩 You should use `SQLAlchemy` 1.3.x
- 🚩 The length of your files will be tested using `wc`
- 🚩 All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- 🚩 All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- 🚩 A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- 🚩 All your functions should be type annotated
- 🚩 The flask app should only interact with `Auth` and never with `DB` directly.
- 🚩 Only public methods of `Auth` and `DB` should be used outside these classes.

## Setup
You will need to install `bcrypt`
```
pip3 install bcrypt
```

By **Estefania Ruiz** 🦌 From **Holberton School** 🪐