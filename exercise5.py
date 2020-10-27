def isAdult(user):
    return user.age >= 18

class User:
    def __init__(self, age):
        self.age = age

user = User(14)
user2 = User(23)

result1 = isAdult(user)
result2 = isAdult(user2)

print(result1, result2)