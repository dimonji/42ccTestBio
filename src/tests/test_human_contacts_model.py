"""
Human models test case
"""
from bio.models import Contacts
from bio.models import Human
from tddspry.django import DatabaseTestCase
from test_human_model import NAME, SURNAME, BIO, BIRTHDAY

import settings

EMAIL = "dimonji@gmail.com"
JABBER = "dimonji@jabber.org"
SKYPE = "fdimonji"
OTHER = "ICQ: 270318081"
NEW_SKYPE = "Dimonji"


class TestModelContacts(DatabaseTestCase):
    """
    Human cread read delete test case
    """
    def test_create(self):
        """
        Test database creation
        """
        human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                   birthday=BIRTHDAY, biography=BIO)
        self.assert_create(Contacts, human=human, email=EMAIL, jabber=JABBER,
                           skype=SKYPE, other=OTHER)

    def test_read(self):
        """
        Test read from database
        """
        human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                   birthday=BIRTHDAY, biography=BIO)
        self.assert_create(Contacts, human=human, email=EMAIL, jabber=JABBER,
                           skype=SKYPE, other=OTHER)
        self.assert_read(Contacts, human=human, email=EMAIL, jabber=JABBER,
                         skype=SKYPE, other=OTHER)

    def test_update(self):
        """
        Test update database row
        """
        human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                   birthday=BIRTHDAY, biography=BIO)
        test_contact = self.assert_create(Contacts, human=human, email=EMAIL,
                                          jabber=JABBER, skype=SKYPE,
                                          other=OTHER)
        self.assert_update(test_contact, email=NEW_SKYPE)

    def test_delete(self):
        """
        Test delete data from database
        """
        human = self.assert_create(Human, name=NAME, surname=SURNAME,
                                   birthday=BIRTHDAY, biography=BIO)
        test_contact = self.assert_create(Contacts, human=human, email=EMAIL,
                                          jabber=JABBER, skype=SKYPE,
                                          other=OTHER)
        self.assert_delete(test_contact)
