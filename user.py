# user.py
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_vote(self):
        return self.age >= 18

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user = User(name, age)
    if user.can_vote():
        print(f"{user.name} can vote.")
    else:
        print(f"{user.name} cannot vote.")