# from app.views import app
# import unittest
# import json
#
#
# class FlaskEventsTest(unittest.TestCase):
#     """views test class"""
#
#     def setUp(self):
#         """ setup fixture for testing """
#         self.app = app.test_client()
#         self.user = {
#             "name": "testname",
#             "email": "testemail@gmail.com",
#             "password": "12345678",
#             "confirm": "12345678"
#         }
#
#         self.event = {
#             "_id": 123456,
#             "name": "talanta",
#             "description": "awesome",
#             "category": "social",
#             "date": "12/34/45",
#             "author": "beth",
#             "location": "nairobi"
#         }
#         self.rsvp = {
#             "_id": 56789,
#             "name": "beth",
#             "email": "bethwambuimuniu@gmail.com",
#             "phone_no": 754234567556,
#             "category": 'guest'
#         }
#
#     def test_register(self):
#         """tests if user is successfully registered"""
#         result = self.app.post('/api/v1/auth/register', data=dict(self.user))
#         self.assertEqual(result.status_code, 201)
#         # self.assertIn('successfully registered', str(result.data))
#
#     def test_login(self):
#         """tests if user is successfully login returns right status code"""
#         self.test_register()
#         user_data = {"email": "testname", "password": "12345678"}
#         result = self.app.post('/api/v1/auth/login', data=dictuser_data)
#         self.assertEqual(result.status_code, 200)
#         # self.assertIn('Successfully logged in', str(result.data))
#
#     def test_create_event(self):
#         """tests if event is created"""
#         self.test_login()
#         resp = self.app.post('/api/v1/events', data=self.event)
#         self.assertEqual(resp.status_code, 201)
#         self.assertIn(' event succesfully created ', str(resp.data))
#
#     def test_view_events(self):
#         """tests if user can view events"""
#         self.test_login()
#         self.test_create_event()
#         resp = self.app.get('/api/v1/events', data=self.event)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_update_events(self):
#         """tests if event is successfully updated"""
#         self.test_login()
#         user_data = {
#             "name": "masaku",
#             "description": "awesome",
#             "category": "social",
#             "date": "12/34/45",
#             "author": "beth",
#             "location": "nairobi"
#         }
#         resp = self.app.put('/api/v1/events/123456', data=user_data)
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn("event successfully edited", str(resp.data))
#
#     def test_delete_events(self):
#         """tests if event is deleted successfully"""
#         self.test_login()
#         resp = self.app.delete('/api/v1/events/123456', data=self.event)
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn("event deleted", str(resp.data))
