class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()

    def menu(self):
        print("Welcome to the Chatbook!! \n" \
        "How would like to proceed? \n" \
        "Press 1. to Signup \n" \
        "Press 2. to Signin \n" \
        "Press 3. to write a post \n" \
        "Press 4. to message a friend \n" \
        "Press any other key to exit \n")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Enter your password here ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully \n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            while (True):
                email = input("Enter your email/username here -> ")
                pwd = input("Enter your password here ->")
        
                if email == self.username and pwd == self.password:
                    print("Congratulations You have signed up successfully!! \n")
                    self.logged_in = True
                    break
                else:
                    print("Please enter the correct credentials \n")
        self.menu()

    def my_post(self):
        if self.logged_in == True:
            post = input("Enter your post here: ")
            print(f"Following content is posted {post}")
        else:
            print("Please Signin first to post on Chatbook.. \n")
        self.menu()

    def send_msg(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            frnd = input("Enter your friend name:")
            print(f"The Following message {txt} is sent to {frnd}")
        else:
            print("Please Signin first to send message on Chatbook.. \n")
        self.menu()

obj = Chatbook()