""" modules and libraries used for TestRsvp class"""
import unittest
from main.rsvp import Rsvp
from main.person import Person


class TestRsvp(unittest.TestCase):
    """ Rsvp Test class """

    def setUp(self):
        """ setup fixture for testing """
        self.beth = Rsvp("beth", "bethwambuimuniu@gmail.com", 754234567556,
                         'guest')

    def test_rsvp_inherits_person(self):
        """ tests if user is a subclass of person """
        self.assertTrue(issubclass(Rsvp, Person))
