class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        pass

    def age(self, current_year):
        age = current_year - self.birth_year
        return age

user = User('Sam', 1998)
print(user.age(2024))
print(user.get_name())