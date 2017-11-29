""" modules and libraries """

import unittest
from app.main.person import Person
from app.main.event import Event
from app.main.user import User


class TestUser(unittest.TestCase):
    """ User Test class """
    def setUp(self):
        """ setup fixture for testing """
        self.beth = User("beth",
                         "bethwambuimuniu@gmail.com",
                         123, "organizer")
        self.beth._id = ("558899")
        self.talanta = Event("talanta",
                             "awesome",
                             "social",
                             "12/34/45",
                             "beth",
                             "nairobi",
                             "558899")
        self.beth.events = {"123456": self.talanta}



    def test_user_inherits_person(self):
        """ tests if user is a subclass of person """
        self.assertTrue(issubclass(User, Person))

    def test_create_event(self, message='event created succesfully'):
        """ tests if adding  event successful """
        result = len(self.beth.events)
        self.beth.create_event("talanta",
                               "fdsa",
                               "social",
                               "12/3/16",
                               "beth",
                               "nairobi",
                               "558899")
        new_result = len(self.beth.events)
        self.assertEqual(new_result, 2)

    def test_update_event(self):
        """ tests if update  event successful """
        self.beth.update_event("123456",
                               "talanta events",
                               "social",
                               "awesome",
                               "123",
                               "beth",
                               "kisumu")
        self.assertEqual("talanta events", self.talanta.name)

    def test_delete_event(self):
        """ tests if delete  event successful """
        self.beth.delete_event("123456")
        new_result = len(self.beth.events)
        self.assertEqual(new_result, 0)
