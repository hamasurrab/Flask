# string are immutuable


fname="hamas"
lname="chaudhary "
chose="cric"

# slicing----method
print(fname[:2])

# my_name capital
print(fname[0].upper())

# print("mr. fname_lname chose")                     #-----1 method
print("MR. {}_{} {}".format(fname,lname,chose))      #------2 method
print(f"Mr.{fname}_{lname} {chose}")


# spilit---------->>>>method
my_string="today kohli made is 71 century"
print(my_string.split("o"))