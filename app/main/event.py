from .rsvp import Rsvp
from uuid import uuid4


class Event:
    """ main class for Event """

    def __init__(self, name, description, category, date, author,
                 location, owner_id):
        self.name = name
        self.description = description
        self.category = category
        self.date = date
        self._id = uuid4().hex
        self.author = author
        self.location = location
        self.owner_id = owner_id
        self.rsvps = dict()

    def events_data(self):
        """returns events """
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "date": self.date,
            "_id": self._id,
            "author": self.author,
            "location":self.location,
            "owner_id":self.owner_id
        }


    def add_rsvp(self, name, email, phone_no, rsvp_category):
        """ add an rsvp to the event """
        new_rsvp = Rsvp(phone_no, name, email, rsvp_category)
        self.rsvps[new_rsvp._id] = new_rsvp
        return self.rsvps[new_rsvp._id]

    def update_rsvp(self, _id, name, email, phone_no, rsvp_category):
        """ edit an rsvp to the event """
        for key in self.rsvps.copy().keys():
            if _id == key:
                self.rsvps[key].name = name
                self.rsvps[key].phone_no = phone_no
                self.rsvps[key].email = email
                self.rsvps[key].rsvp_category = rsvp_category

    def delete_rsvp(self, _id):
        """ deletes an rsvp to the event """
        for key in self.rsvps.copy().keys():
            if _id == key:
                del self.rsvps[_id]

    def __repr__(self):
        """ Return formatted event object"""
        return '<Event {}>'.format(self.name)
