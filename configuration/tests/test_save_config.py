import inspect
import json

from configuration.configuration import ConfigurationHelper
from unittest import TestCase
from inspect import getmembers_static, isroutine


class TestClassConfigurationSpecifications:
    # There configurations are static in a better approach you have to submit them manually
    EthereumTestNetNodeProvider = str("Hey01")
    EthereumMainNetNodeProvider = str("Hey02")


class TestSaveConfigurations(TestCase):
    def test_save_config(self):
        attributes = ConfigurationHelper.get_class_attributes(TestClassConfigurationSpecifications)
        ConfigurationHelper.save_configurations(TestClassConfigurationSpecifications, "./configurations.json",
                                                **attributes)
        print(attributes)

    def test_save_config_02(self):
        attributes = ConfigurationHelper.get_class_attributes(TestClassConfigurationSpecifications)
        attributes[ConfigurationHelper.get_class_attribute_name(TestClassConfigurationSpecifications,
                                                                TestClassConfigurationSpecifications.EthereumTestNetNodeProvider)] = "ManuallyHandled"
        ConfigurationHelper.save_configurations(TestClassConfigurationSpecifications, "./configurations.json",
                                                **attributes)
        print(attributes)
