"""
Human models test case
"""
from bio.models import Human
from tddspry.django import DatabaseTestCase

import settings
NAME = "Dmitry"
SURNAME = "Furzenko"
BIRTHDAY = "1984-09-21"
NEW_NAME = "D"

class TestModelHuman(DatabaseTestCase):
    """
    Human cread read delete test case
    """
    def test_create(self):
        """
        Test database creation
        """
        self.assert_create(Human, name=NAME, surname=SURNAME, birthday=BIRTHDAY)

    def test_read(self):
        """
        Test read from database
        """
        self.assert_create(Human, name=NAME, surname=SURNAME, birthday=BIRTHDAY)
        self.assert_read(Human, name=NAME, surname=SURNAME, birthday=BIRTHDAY)

    def test_update(self):
        """
        Test update database row
        """
        test_human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                        birthday=BIRTHDAY)
        self.assert_update(test_human, name=NEW_NAME)

    def test_delete(self):
        """
        Test delete data from database
        """
        test_human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                        birthday=BIRTHDAY)





