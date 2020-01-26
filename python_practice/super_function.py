"""
Description :  Checking the super function in python
"""


class Computer():
    def __init__(self, computer, ram):
        self.computer = computer
        self.ram = ram


class Laptop(Computer):
    def __init__(self, computer, ram, model):
        self.model = model


class Macbook(Computer):
    def __init__(self, computer, ram, model):
        super().__init__(computer, ram)
        self.model = model


# the following line will throw error
lenovo = Laptop("lenovo", 2, "T480s")
try:
    print(f"lenovo laptop config is:{lenovo.computer}, {lenovo.ram} and {lenovo.model}")
except AttributeError as error:
    print(f"attribute error happened:{error}")
# the following line will works
mac = Macbook("mac", 4, "macbook pro")
print(f"mac book config is:{mac.computer}, {mac.ram} and {mac.model}")