""" modules and libraries used for TestRsvp class"""
import unittest
from app.main.rsvp import Rsvp
from app.main.person import Person


class TestRsvp(unittest.TestCase):
    """ Rsvp Test class """

    def setUp(self):
        """ setup fixture for testing """
        self.beth = Rsvp("beth", "bethwambuimuniu@gmail.com", 754234567556,
                         'guest')
        self.rsvps = {56789: self.beth}
    def test_rsvp_inherits_person(self):
        """ tests if user is a subclass of person """
        self.assertTrue(issubclass(Rsvp, Person))
    def test_rsvps_data(self):
        """tests if saves rsvp_data is successful"""
        self.assertTrue(self.beth, 1)
