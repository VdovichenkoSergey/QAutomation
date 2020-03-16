import unittest
from Profile.ITEmployee import ITemployee


class TestITemployee(unittest.TestCase):

    def setUp(self):
        self.user = ITemployee('qa', 4, 1500, 'Serhio Brugeiro', 1985, 'Java', 'Python')

    def test_add_skill(self):
        self.user.add_skill('qwerty')
        self.assertIn('qwerty', self.user.skills)

    def test_add_skills(self):
        self.user.add_skills('111', '222')
        self.assertIn('111' and '222', self.user.skills)