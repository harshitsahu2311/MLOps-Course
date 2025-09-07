#1 - Here the variable the user_id is not static means every time initialize with zero

# class Chatbook:
#     def __init__(self):
#         self.__username = 'Default User'
#         self.user_id = 0
#         self.user_id += 1
#         self.password = ''
#         self.logged_in = False
#         # self.menu()

#     def get_name(self):
#         return self.__username
    
#     def set_name(self, value):
#         self.__username=value

# obj = Chatbook()

# now run the access_9 file code of #1

#2 Let's make the variable the static 

# class Chatbook:

#     __user_id = 0
#     def __init__(self):
#         self.__username = 'Default User'
#         self.id = Chatbook.__user_id
#         Chatbook.__user_id+=1
#         self.password = ''
#         self.logged_in = False
#         # self.menu()

#     def get_name(self):
#         return self.__username
    
#     def set_name(self, value):
#         self.__username=value

# obj = Chatbook()

# now again run the access_9 file code of #2

#3 Static Method for getter and setter

class Chatbook:

    __user_id = 0
    def __init__(self):
        self.__username = 'Default User'
        self.id = Chatbook.__user_id
        Chatbook.__user_id+=1
        self.password = ''
        self.logged_in = False
        # self.menu()

    @staticmethod
    def get_id():
        return Chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        Chatbook.__user_id = value
        return Chatbook.__user_id

obj = Chatbook()

# now run #3 of the access_9