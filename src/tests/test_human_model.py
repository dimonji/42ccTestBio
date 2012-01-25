"""
Human models test case
"""
from bio.models import Human
from tddspry.django import DatabaseTestCase


NAME = "Dmitry"
SURNAME = "Furzenko"
BIRTHDAY = "1984-09-21"
BIO = "To be or not to be..."
NEW_NAME = "D"


class TestModelHuman(DatabaseTestCase):
    """
    Human cread read delete test case
    """
    def test_create(self):
        """
        Test database creation
        """
        self.assert_create(Human, name=NAME, surname=SURNAME,
                           birthday=BIRTHDAY, biography=BIO)

    def test_read(self):
        """
        Test read from database
        """
        self.assert_create(Human, name=NAME, surname=SURNAME,
                           birthday=BIRTHDAY, biography=BIO)
        self.assert_read(Human, name=NAME, surname=SURNAME, birthday=BIRTHDAY,
                         biography=BIO)

    def test_update(self):
        """
        Test update database row
        """
        test_human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                        birthday=BIRTHDAY, biography=BIO)
        self.assert_update(test_human, name=NEW_NAME)

    def test_delete(self):
        """
        Test delete data from database
        """
        test_human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                        birthday=BIRTHDAY, biography=BIO)
        self.assert_delete(test_human)
