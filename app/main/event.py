from .rsvp import Rsvp
from uuid import uuid4
import datetime


class Event:
    """ main class for Event """

    def __init__(self, name, description, category, date, author, location):
        self.name = name
        self.description = description
        self.category = category
        self.id = uuid4().hex
        self.author = author
        self.location = location
        self.rsvps = dict()

    def add_rsvp(self, phone_no, name, email, rsvp_category):
        """ add an rsvp to the event """
        new_rsvp = Rsvp(phone_no, name, email, rsvp_category)
        self.rsvps[new_rsvp.id] = new_rsvp
        return self.rsvps[new_rsvp.id]

    def update_rsvp(self, _id, phone_no, name, email, rsvp_category):
        """ edit an rsvp to the event """
        for key in self.rsvps.copy().keys():
            if _id == key:
                self.events[key].name = name
                self.events[key].phone_no = phone_no
                self.events[key].email = email
                self.events[key].rsvp_category = rsvp_category

    def delete_rsvp(self, _id):
        """ deletes an rsvp to the event """
        for key in self.rsvps.copy().keys():
            if _id == key:
                del self.rsvps[_id]
