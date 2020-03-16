from Profile.Employee import Employee


class ITemployee(Employee):

    def __init__(self, position, experience, salary, full_name, year_of_birth, *skills):
        Employee.__init__(self, position, experience, salary, full_name, year_of_birth)
        self.skills = list(skills)

    def add_skill(self, skill_new):
        self.skills.append(skill_new)

    def add_skills(self, *skills_new):
        # self.skills_new = list(skills_new)
        self.skills.extend(list(skills_new))

    def __str__(self):
        message = f'Atributes of your object: \n \n'\
                  f'Full name: {self.full_name} \n'\
                  f'Year of birth: {self.year_of_bitrh} \n'\
                  f'Position: {self.position} \n'\
                  f'Skills: {self.skills} \n'\
                  f'Experience: {self.experience} \n'\
                  f'Salary: {self.salary} \n'
        return message



c = ITemployee('qa', 4, 1500, 'Serhio Brugeiro', 1985, 'Java', 'Python')
#
# print(c)
# print(c.skills)
#
# c.add_skill('Selenium')
# print(c.skills)
#
# c.add_skills('delpi', 'C++')
# print(c.skills)
# print(c)

