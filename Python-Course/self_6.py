#1

# class employee:
#     # special method/magic method/dunder method - constructor
#     def __init__(self):
#         print(id(self)) # memory address of self pointer
#         self.id = 1
#         self.salary = 1000000
#         self.designation = "DevOps Engineer"

# #create an obj/instance of the class
# sam = employee()
# print(id(sam))

# # here we can see memory address of sam and self points to same, means obj only is passed in each method of class

#2

# class employee:
#     def __init__(self):
#         print(id(self))
#         self.id = 123
#         self.salary = 50000
#         self.designation = "Cloud Engineer"
    
#     def travel(destination):
#         print(f"employee is now travelling to {destination}")

# sam = employee()
# print(id(sam))
# sam.travel("Mumbai")

# # here we get an error typeerror for not passing an positional variable in travel method

#3

# class employee:
#     # special method/magic method/dunder method - constructor
#     def __init__(self):
#         print(id(self)) # memory address of self pointer
#         self.id = 1
#         self.salary = 1000000
#         self.designation = "DevOps Engineer"

# #create an obj/instance of the class
# sam = employee()
# print(id(sam))

# shakti = employee()
# print(id(shakti))

#4 
# You can also create an attribute outside an class

class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print(id(self)) # memory address of self pointer
        self.id = 1
        self.salary = 1000000
        self.designation = "DevOps Engineer"

#create an obj/instance of the class
sam = employee()
sam.name = 'SAM KUMAR'
print(sam.name)