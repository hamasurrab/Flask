# METHODS AND INHERITANCE
class circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
# METHODS
    def area(self):
        return self.radius*self.radius*self.pi


x = circle(11)
print(x.radius)
print(x.area())
