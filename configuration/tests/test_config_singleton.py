import json
from unittest import TestCase
from configuration.configuration import ConfigurationHelper


class TestClassConfigClass:
    EthereumNodeProvider = str()
    Secret = str()


class TestClassConfigSingleton:
    def __init__(self, ethereum_node_provider: str, secret: str):
        self.ethereum_node_provider = ethereum_node_provider
        self.secret = secret

    def call_settings(self):
        print(self.ethereum_node_provider, self.secret)


class TestConfigSingleton(TestCase):
    def test_config_singleton(self):
        config_helper = ConfigurationHelper("./configurations.json")
        new_class = config_helper.config_singleton(TestClassConfigSingleton, TestClassConfigClass)
        print(json.dumps(new_class.__dict__))
