"""Modules and libraries used for Test Person class."""
import unittest
from app.main.person import Person


class TestPerson(unittest.TestCase):
    """Person Test class"""

    def setUp(self):
        """Setup fixture for testing."""
        self.beth = Person("beth", "bethwambuimuniu@gmail.com" 'guest')
