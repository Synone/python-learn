class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User created")
    def __repr__(self) -> str:
        return "User(username = '{}', name='{}', email='{}')".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()


 
user1 = User("sonyne","Sony","syno3311@gmail.com")
print(user1.email)
user1.introduce_yourself("Sony")
