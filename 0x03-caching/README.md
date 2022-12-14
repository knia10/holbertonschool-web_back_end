# 0x03. Caching
<img src="https://www.ogmaconceptions.com/wp-content/uploads/2019/05/python-development-vector.png" width = 500px length = 500px >

### General π
- π What a caching system is
- π What FIFO means
- π What LIFO means
- π What LRU means
- π What MRU means
- π What LFU means
- π What the purpose of a caching system
- π What limits a caching system have
## Requirements
#### Python Scripts
- π° All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- π° All your files should end with a new line
- π° The first line of all your files should be exactly `#!/usr/bin/env` python3
- π° A `README.md` file, at the root of the folder of the project, is mandatory
- π° Your code should use the `pycodestyle` style (version 2.5)
- π° All your files must be executable
- π° The length of your files will be tested using `wc`
- π° All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- π° All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- π° All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- π° A documentation is not a simple word, itβs a real sentence explaining whatβs the purpose of the module, class or method (the length of it will be verified)
### More Info
#### Parent class BaseCaching
All your classes must inherit from `BaseCaching` defined below:
```
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

**From Holberton School** β¨ **By Estefania Ruiz** πΉ