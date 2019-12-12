from unittest import TestCase

import caselaw-tools

class TestHello(TestCase):
    def test_is_string(self):
        s = caselaw-tools.hello()
        self.assertTrue(isinstance(s, basestring))