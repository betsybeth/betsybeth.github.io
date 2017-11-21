""" modules and libraries used for Test Person class"""
import unittest
from main.person import Person

class TestPerson(unittest.TestCase):
    """ Person Test class """
    def setUp(self):
        self.beth = Person("beth", "bethwambuimuniu@gmail.com" 'guest')
