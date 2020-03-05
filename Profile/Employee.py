from Profile.Person import Person


class Employee(Person):

    def __init__(self, position, experience, salary, full_name, year_of_birth):
        Person.__init__(self, full_name, year_of_birth)
        self.position = position
        self.experience = experience
        self.salary = salary

    def pre_position(self):
        if self.experience < 3:
            return f"Junior {self.position}"
        elif self.experience >= 3 and self.experience <= 6:
            return f"Middle {self.position}"
        else:
            return f"Senior {self.position}"

    def rise_salary(self, rise):
        self.rise = rise
        return f'New salary: {self.salary + self.rise}'


b = Employee(position='QA', experience=6.5, salary=2100, full_name='Sergey Vdovichenko', year_of_birth=1981)
# print(b.pre_position())
# print(b.rise_salary(200.20))



