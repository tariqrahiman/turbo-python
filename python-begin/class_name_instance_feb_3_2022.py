# Sample Python Program to get the Class Name of an Instance
# __class__ is the attribute of the class to which it is associated and __name__ is a special variable
# Author : Tariq Rahiman

class Sports:
    def name(self, name):
        return name

v = Sports()
print(v.__class__.__name__)
