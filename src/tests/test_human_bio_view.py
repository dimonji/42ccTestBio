from tddspry.django import HttpTestCase


class TestHumanBioView(HttpTestCase):
    """
    Test bio.views
    """
    def test_context_processor(self):
        self.go200("/")
        self.find("Dmitry")
