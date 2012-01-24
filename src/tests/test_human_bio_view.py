from tddspry.django import HttpTestCase


class TestHumanBioView(HttpTestCase):
    """
    Test bio.views
    """
    def test_context_processor(self):
        self.go200("/")
        self.find("Dmitry")
        self.find("Furzenko")
        self.find("dimonji@gmail.com")
        self.find("270318081")
