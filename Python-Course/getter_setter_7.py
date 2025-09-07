class Chatbook:
    def __init__(self):
        self.__username = 'Default User'
        self.password = ''
        self.logged_in = False
        # self.menu()

    def get_name(self):
        return self.__username
    
    def set_name(self, value):
        self.__username=value

obj = Chatbook()