from app.views import app
import os
import unittest
import json


class FlaskEventsTest(unittest.TestCase):
    """"""

    def setUp(self):
        self.app = app.test_client()
        self.user = {
            "name":"testname",
            "email": "testemail@gmail.com",
            "password": "12345678",
            "confirm": "12345678"
        }

        self.event = {
            "name": "talanta",
            "description": "awesome",
            "category": "social",
            "date": "12/34/45",
            "author": "beth",
            "location": "nairobi"
        }
        self.rsvp = {
            "name": "beth",
            "email": "bethwambuimuniu@gmail.com",
            "phone_no": 754234567556,
            "category": 'guest'
        }


    def test_register(self):
        result = self.app.post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code, 201)
        self.assertIn('successfully registered', str(result.data))

    def test_login(self):
        self.test_register()
        user_data= {"email":"testname", "password":"12345678"}
        result = self.app.post('/api/v1/auth/login', data=user_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Successfully logged in', str(result.data))
    def test_create_event(self):
        self.test_login()
        resp = self.app.post('/api/v1/events', data=self.event)
        self.assertEqual(resp.status_code, 201)
        self.assertIn(' event succesfully created ', str(resp.data))
    def test_view_events(self):
        self.test_login()
        self.test_create_event()
        resp = self.app.get('/api/v1/events', data=self.event)
        self.assertEqual(resp.status_code, 200)
    def test_update_events(self):
        self.test_login()
        user_data={"name": "masaku","description": "awesome","category": "social","date": "12/34/45",
                   "author": "beth","location": "nairobi"}
        resp = self.app.put('/api/v1/events/123456', data=user_data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("event successfully edited", str(resp.data))
    def test_delete_events(self):
        self.test_login()
        resp = self.app.delete('/api/v1/events/123456', data=self.event)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("event deleted", str(resp.data))

    def test_create_rsvp(self):
        self.test_login()
        self.test_create_event()
        resp = self.app.post('/api/v1/event/123456/rsvp', data=self.rsvp)
        self.assertEqual(resp.status_code, 201)
        self.assertIn("rsvp created successfully", str(resp.data))
