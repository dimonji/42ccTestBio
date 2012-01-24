"""
Human models test case
"""
from bio.models import Contacts
from tddspry.django import DatabaseTestCase

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
        self.assert_create(Contacts, email=EMAIL, jabber=JABBER, skype=SKYPE,
                           other=OTHER)

    def test_read(self):
        """
        Test read from database
        """
        self.assert_create(Contacts, email=EMAIL, jabber=JABBER, skype=SKYPE,
                           other=OTHER)
        self.assert_read(Contacts, email=EMAIL, jabber=JABBER, skype=SKYPE,
                         other=OTHER)

    def test_update(self):
        """
        Test update database row
        """
        test_contact = self.assert_create(Contacts, email=EMAIL, jabber=JABBER,
                                        skype=SKYPE, other=OTHER)
        self.assert_update(test_contact, email=NEW_EMAIL)

    def test_delete(self):
        """
        Test delete data from database
        """
        test_contact = self.assert_create(Contacts, email=EMAIL, jabber=JABBER,
                                          skype=SKYPE, other=OTHER)
        self.assert_delete(test_contact)





