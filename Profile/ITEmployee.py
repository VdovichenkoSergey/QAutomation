from Profile.Employee import Employee


class ITemployee(Employee):

    def __init__(self, *skills, experience, salary, full_name, position, year_of_birth):
        Employee.__init__(self, experience, salary, full_name, position, year_of_birth)
        self.skills = list(skills)

    def add_skill(self, skill_new):
        return self.skills.append(skill_new)

    def add_skills(self, *skills_new):
        # self.skills_new = list(skills_new)
        return self.skills.extend(list(skills_new))

    def __str__(self):
        message = f'Atributes of your object: \n'\
                  f'Full name: {self.full_name} \n'\
                  f'Year of birth: {self.year_of_bitrh} \n'\
                  f'Position: {self.position} \n'\
                  f'Skills: {self.skills} \n'\
                  f'Experience: {self.experience} \n'\
                  f'Salary: {self.salary} \n'\

        return message



c = ITemployee('Java', 'Python', experience=4, salary=1500, full_name='Serhio Brugeiro', position='qa', year_of_birth=1985)

print(c)
# print(c.__str__())
#
# print(c.skills)
#
# c.add_skill('Selenium')
# print(c.skills)
#
# c.add_skills('delpi', 'C++')
# print(c.skills)


