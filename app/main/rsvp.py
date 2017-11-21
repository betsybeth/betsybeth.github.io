""" modules and standard libraries """
from .person import Person
from uuid import uuid4



class Rsvp(Person):
    """ main class for the RSVP """
    def __init__(self, phone_no, name, email, rsvp_category):
        super().__init__(name, email, rsvp_category)
        self.phone_no = phone_no
        self.id = uuid4().hex
