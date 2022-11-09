# ----------DECORATORS-----------
# IT ALLOW to decorate a function


# def hello(name='hamas'):
#     print("hello coders")
    
#     def greet():
#         return "coding club welcome u guyzz"
#     print(greet())  

#     def welcome():
#         return 'welcome mr/mrs'  
#     print(welcome())   

#     if name=='hamas': 
#       return greet
#     else:
#         return welcome  
# x=hello()     
# print(x())

def new_decorator(func):
    def wrap_func():
        print("before executing")
        func()
        print("after executing")
    return wrap_func

@new_decorator
def func_need_decorator():
    print('please decorate me')

func_need_decorator()            