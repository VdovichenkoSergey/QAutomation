class Student:
    def __init__(self, full_name, speciality, year_start, grade_list=[]):
        self.full_name = full_name
        self.speciality = speciality
        self.year_start = year_start
        self.grade_list = grade_list

    def new_grade(self, grade):
        return self.grade_list.append(grade)

    def average_grade(self):
        grade_sum = 0
        for i in self.grade_list:
            grade_sum = grade_sum + i
        return f'Average grade of user: {grade_sum / len(self.grade_list)}'

    def average_grade2(self):
        return f'Average grade of user: {sum(self.grade_list) / len(self.grade_list)}'

    def years_now(self, year):
        return f'Current number of teaching years: {year - self.year_start}'

    def __str__(self):
        message = f'Atributes of your object: \n \n'\
                  f'Full name: {self.full_name} \n'\
                  f'Speciality: {self.speciality} \n'\
                  f'Teaching started in: {self.year_start} \n'\
                  f'Grades: {self.grade_list} \n'
        return message

dude = Student('Vasiliy Terkin', 'Economic', 2017)

dude.new_grade(5)
dude.new_grade(1)
dude.new_grade(12)
dude.new_grade(7)

print(dude.grade_list, '\n')
print(dude.average_grade2(), '\n')
print(dude.years_now(2020), '\n')
print(dude)