class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, mi name is {} and I am {} year old'.format(self.name, self.age))


if __name__ == '__main__':
    person = Person('Luisma', 31)
    person.say_hello()
