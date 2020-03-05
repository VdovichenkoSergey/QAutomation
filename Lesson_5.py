class Person:
    # scope = ['people', 'something']
    def __init__(self, x, y, z):
        self.name = x
        self.age = y
        self.position = z

    def set_name(self, x):
        self.name = x

    def __str__(self):
        return f"<Person with name {self.name}>"

    def __add__(self, other):
        return Person(x=self.name+other.name, y=1, z=2)

p1 = Person('Sergey', 25, 'QA')
print(p1.name, p1.age, p1.position)
p1.set_name('Vasia')
print(p1.name)
p1.name

p2 = Person('Nik', 28, 'QC')
print(p2.name, p2.position, p2.age)
p2.set_name('Kolia')
print(p2.name)

p3 = Person('Olha', 34, 'BA')
print(p3)
p3.__add__(p1.name, p2.name)
print(p3)


class Employee(Person):
    '''Наследование'''

    '''Если создать метод, такой же как в наследуемом классе (например переделать его), 
    то он будет всегда вызываться для этого класса'''

    '''конструктор наследуемого класса'''
    def __init__(self, surname, lastname, y, x, z):
        Person.__init__(self,x , y, z)
        self.name = x
        self.age = y
        self.position = z

    def new_method(x):
        pass