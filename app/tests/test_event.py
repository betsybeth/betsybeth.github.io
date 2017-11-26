""" modules and libraries used for Test Event class """

import unittest
from ..main.event import Event
from ..main.rsvp import Rsvp


class TestEvent(unittest.TestCase):
    """ Event Test class """

    def setUp(self):
        """ setup fixture for testing """
        self.talanta = Event("talanta",
                       "awesome", "social", "12/34/45", "beth", "nairobi", "558899")
        self.beth = Rsvp( "beth", "bethwambuimuniu@gmail.com", "754234567556", 'guest')
        self.beth._id = ("558899")
        self.rsvps = {56789: self.beth}
    def test_event_data(self):
        """tests if saves event data is successful"""
        self.assertTrue(self.talanta, 1)
    def test_add_rsvp(self):
        """ tests if adding of rsvp successful """
        result = len(self.talanta.rsvps)
        self.talanta.add_rsvp("maggie", "maggie@gmail.com", "054532221",
                              "guest")
        new_result = len(self.talanta.rsvps)
        self.assertEqual(new_result, 1)

    def test_update_rsvp(self):
        """ tests if update  rsvp successful """
        self.talanta.update_rsvp(56789, "gigi","magg@gmail.com", "054532221",
                                 "others")
        self.assertEqual("beth", self.beth.name)

    def test_delete_rsvp(self):
        """ tests if delete rsvp successful """
        self.talanta.delete_rsvp(56789)
        new_result = len(self.talanta.rsvps)
        self.assertEqual(new_result, 0)
