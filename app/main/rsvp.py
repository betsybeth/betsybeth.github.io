""" modules and standard libraries """
from .person import Person
from uuid import uuid4



class Rsvp(Person):
    """ main class for the RSVP """
    def __init__(self, name, email, phone_no, rsvp_category):
        super().__init__(name, email, rsvp_category)
        self.phone_no = phone_no
        self._id = uuid4().hex

    def rsvps_data(self):
        """ returns the rsvp"""
        return {
            "_id" :self._id,
             "name":self.name,
             "email": self.email,
             "phone_no":self.phone_no,
             "rsvp_category":self.rsvp_category
        }
