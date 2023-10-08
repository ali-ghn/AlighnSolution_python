from json import dumps
from configuration.configuration import ConfigurationHelper
from unittest import TestCase


class TestClassClassAttribute:
    ClassAttribute01 = str("Hey01")
    ClassAttribute02 = str("Hey02")
    ClassAttribute03 = str("Hey03")
    ClassAttribute04 = str("Hey04")


class TestGetClassAttributes(TestCase):
    def test_get_class_attributes(self):
        attributes = ConfigurationHelper.get_class_attributes(TestClassClassAttribute)
        print(dumps(attributes, indent=4))
