from static_method_9 import Chatbook
user1 = Chatbook()

#1

# print(user1.user_id)

# user2 = Chatbook()
# print(user2.user_id)

# user3 = Chatbook()
# print(user3.user_id)

#2

# print(user1.id)

# user2 = Chatbook()
# print(user2.id)

# user3 = Chatbook()
# print(user3.id)

#3

print(user1.id)

Chatbook.set_id(10)
user2 = Chatbook()
print(user2.id)
