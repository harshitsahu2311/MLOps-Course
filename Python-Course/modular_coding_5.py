#1
# from oops_project_4 import Chatbook
# user1 = Chatbook()

#2
#firstly comment the self.menu() in the def __init__ method of oops_project
# from oops_project_4 import Chatbook
# user1 = Chatbook()
# user1.send_msg()

#3

# In the def __init__() function set self.username = "Default User" keep the self.menu commented in the entire below sample code.
# from oops_project_4 import Chatbook
# user1 = Chatbook()
# print(user1.username)

# So you get an output of 'Default User' but suppose you want to hide this variable to do not access from outside of the code.
# then you can write it in function like this self.__username = 'Default User' and run again the above code of #3

# Whenever you create an object it saves like this:
# emp(id)   ----->   P(obj.id)
# In hidden it stores like this in memory
# emp(__name)  ------>   P(obj._emp__name)

from oops_project_4 import Chatbook
user1 = Chatbook()
print(user1._Chatbook__username)