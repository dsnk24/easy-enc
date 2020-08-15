# EasyEnc, encryption module made for Python.
EasyEnc is a quick, light and easy module made for Python, to ease your encryption needs.

# Installation Instructions
Installing this module is as easy as advertised:

**Method 1**:
    You can run `pip install easyenc` in your CMD/Terminal to download and install it
    directly from PyPI (Python Package Index).

**Method 2**:
    You can download the source code from this repository and after that, running
    `pip install "the/path/to/the/downloaded/repo"`
    in your CMD/Terminal and you're done!


# Usage and Prerequisites
Only requirement this module asks for is the Cryptography module which you can install with
`pip install cryptography`

To use this module, open up a new Python file and type
`from EasyEnc import KeyGenerator, Encryptor`
From there, you can create instances of these classes and use the functions inside them, like:
```
kg = KeyGenerator()
e = Encryptor()

key = kg.generate_key("foobar")
super_top_secret_message = e.encrypt_message("deep dark secret", key)

print(super_top_secret_message)
```

Don't worry you can also decrypt it! But to find out more about it, you can open up a Python Shell and type:
`from EasyEnc.classes import KeyGenerator, Encryptor`
and then:
`help(KeyGenerator)` or `help(Encryptor)`

and Python will display all the available functions along with some documentation included in the source code! 


# Bugs and Issues
If you encounter any bugs with the module, feel free to send me a message on Discord @saint#5622, or email me at erick.8bld@gmail.com