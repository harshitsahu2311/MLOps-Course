class employee:
    def __init__(self):
        print("Started Executing the attributes/data")
        self.id = 1134
        self.salary = 4000000
        self. designation = "SRE"
        print("Attributes have been initiated")
    
    def travel(self, destination):
        print("This travel function is called manually")
        print(f"Employee is traveling to {destination}")

#1
# sam = employee()
#This shows that when we create an object attributes/data are initiated automatically but methods we have to call manually.

#2
# sam = employee()
# sam.travel("Bangalore")

#3
# sam = employee()
# print(type(sam))

#similarly all the python modules are class like list, tuple, dictionary, ini, float etc.

#4
lst = [1,2,4,6]
my_str = "Harshit Sahu"
my_int = 143

print(type(lst))
print(type(my_str))
print(type(my_int))

lst.clear()  # these are the methods of the class list
print(lst)

lst.Captialize()