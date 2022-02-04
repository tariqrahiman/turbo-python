# Sample Python Program to get the Class Name of an Instance
# type() gives the class of object v and __name__ gives the class name
# Author : Tariq Rahiman

class Sports:
    def name(self, name):
        return name

v = Sports()
print(type(v).__name__)