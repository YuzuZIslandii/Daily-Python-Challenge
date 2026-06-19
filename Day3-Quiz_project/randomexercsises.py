class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user has been created")

    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"{self.username} is now following {user.username}")



user_1 = User(1, "John")
user_2 = User(2, "Jane")

users = [user_1, user_2]

user_1.follow(user_2)

for each in users:
    print(f"User: {each.username} with id: {each.id}. They have {each.followers} followers and are following {each.following} users.")