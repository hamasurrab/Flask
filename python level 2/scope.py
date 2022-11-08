# concept that determine where you can see or access a variable

x="outside"

def report():
    x="inside"
    return x
print(x)


# LEGB RULE
# 1->local
# 2->ENCLOSING
# 3->GLOBAL
# 4->BUILT IN