""" modules and libraries used for Test Event class """

import unittest
from ..main.event import Event
from ..main.rsvp import Rsvp


class TestEvent(unittest.TestCase):
    """ Event Test class """

    def setUp(self):
        """ setup fixture for testing """
        self.talanta = Event("talanta",
                       "awesome", "social", "12/34/45", "beth", "nairobi")
        self.beth = Rsvp("754234567556", "beth", "bethwambuimuniu@gmail.com",
                         'guest')
        self.rsvps = {56789: self.beth}

    def test_add_rsvp(self):
        """ tests if adding of rsvp successful """
        result = len(self.talanta.rsvps)
        self.talanta.add_rsvp("054532221", "maggie", "maggie@gmail.com",
                              "guest")
        new_result = len(self.talanta.rsvps)
        self.assertEqual(new_result, 1)

    def test_update_rsvp(self):
        """ tests if update  rsvp successful """
        self.talanta.update_rsvp(56789, "054532221", "gigi", "magg@gmail.com",
                                 "others")
        self.assertEqual("beth", self.beth.name)

    def test_delete_rsvp(self):
        """ tests if delete rsvp successful """
        self.talanta.delete_rsvp(56789)
        new_result = len(self.talanta.rsvps)
        self.assertEqual(new_result, 0)
