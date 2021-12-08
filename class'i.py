class User:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

        self.height = None

    def show(self):
        print(f'This user name is {self.name} and his age is {self.age}'
              f' and his phone is {self.phone}')


class Teacher(User):
    def __init__(self, name, age, phone, stazh):
        super(Teacher, self).__init__(name, age, phone)
        self.stazh = stazh

    def show(self):
        super().show()
        print('Also he is a teacher')


teacher = Teacher('Timur', 21, '+12345', 3)
user = User("Alya", 17, "+125")
user.name = "Timur"
user.height = "1.5"

user.show()