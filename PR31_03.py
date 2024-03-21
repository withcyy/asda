class Human:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count += 1

    @staticmethod
    def get_instance_count():
        return Human.count

human1 = Human("Alex", 30)
human2 = Human("Vlad", 25)
human3 = Human("Петро", 35)

print(Human.get_instance_count())