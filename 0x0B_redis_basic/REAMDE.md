# 0x0B. Redis basic
<img src="https://miro.medium.com/max/1200/0*bFwO2Ep7bguEenTO.png" width = 600px length = 300px >

## Learning Objectives📖
- 🔰 Learn how to use redis for basic operations
- 🔰 Learn how to use redis as a simple cache

## Requirements
- 🚩 All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- 🚩 All your files should end with a new line
- 🚩 A `README.md` file, at the root of the folder of the project, is mandatory
- 🚩 The first line of all your files should be exactly `#!/usr/bin/env python3`
- 🚩 Your code should use the `pycodestyle` style (version 2.5)
- 🚩 All your *.py files should be executable
- 🚩 All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- 🚩 All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- 🚩 A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- 🚩 All your functions should be type-annotated

## Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
By **Estefania Ruiz** 🦌 From **Holberton School** 🪐