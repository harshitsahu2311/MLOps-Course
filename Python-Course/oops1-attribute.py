class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 1
        self.salary = 1000000
        self.designation = "DevOps Engineer"

#create an obj/instance of the class
sam = employee()
print(sam.id)