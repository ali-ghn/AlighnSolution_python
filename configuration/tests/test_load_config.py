import json

from configuration.configuration import ConfigurationHelper
from unittest import TestCase


class TestClassConfigurationSpecifications:
    EthereumTestNetNodeProvider = str()
    EthereumMainNetNodeProvider = str()


class TestLoadConfigurations(TestCase):
    def test_load_config(self):
        configs = ConfigurationHelper.get_configurations(TestClassConfigurationSpecifications, "./configurations.json")
        print(json.dumps(configs, indent=4))
