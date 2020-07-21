#this is an example of a custom class python 

class Point():
    def __init__(self, input1, input2):   # constructor method/function which is automatically called every time a new 'Point' object is called
        self.x = input1
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)


