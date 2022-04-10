#PascalCase, camelCase, snake_case
class User:

    def __init__(self, user_id, username):
        print("new user being created..")
        self.id = user_id #object.attribute = parameter
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

#Constructor - Part of the blueprint which specifies what happens when an object is Constructed
# Also called INITIALIZE

# Creating Object
user_1 = User("001","sahithi")
user_2 = User("002","vineeth")
print(user_1.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)