class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Cloud Engineer"
    
    def travel(self, destination):
        print(f"employee is now travelling to {destination}")

sam = employee()
sam.travel("Mumbai")