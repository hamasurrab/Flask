# -----------------object oriented progrraming--------------------------
# it allow programmer to create their own object that have method and attribute
class dog():

#  CLASS OBJECT ATTRIBUTE
    def __init__(self, input_breed,input_name):
        self.breed = input_breed
        self.name=input_name

x = dog('huskie','julie')

print(x.breed)
print(x.name)
