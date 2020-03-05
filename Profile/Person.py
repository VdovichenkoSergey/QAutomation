class Person:
    def __init__(self, full_name, year_of_birth):
        self.full_name = str(full_name)
        self.year_of_bitrh = int(year_of_birth)
        self.name_parsing = self.full_name.split()

    def first_name(self):
        f_name1 = self.name_parsing[0]
        return f_name1

    def surname(self):
        surname = self.name_parsing[1]
        return surname

    def age_in(self, year_in=2020):
        years_old = year_in - self.year_of_bitrh
        return years_old


#a = Person('Sergey Vdovichenko', 1981)
# print(a.first_name())
# print(a.surname())
# print(a.year_of_bitrh)
# print(a.age_in(2024))






