from inspect import getmembers_static, isroutine
from json import load, dump
import re
from exceptions.configuration_exceptions import ConfigurationExceptions


class ConfigurationHelper:
    def __init__(self, configuration_file_location: str):
        """
        Configuration Helper will enable dependency-injection in a very convenient way.
        :param configuration_file_location: hence the name it requires configuration file location
        """
        self.configuration_file_location = configuration_file_location

    def __int__(self):
        """
        If configuration helper is not required to handle dependency-injection it does not require the path but
        all the methods are static so there is no need for such an initialization.
        :return:
        """
        self.configuration_file_location = None

    @staticmethod
    def get_configurations(target_class, configuration_file_location: str) -> dict:
        """
        get_configuration will load the config from a file using the blueprint that target_class has provided.
        :param target_class: the class which configs should be loaded from their static attributes.
        :param configuration_file_location: hence the name it requires configuration file location.
        :return:
        """
        members = getmembers_static(target_class)
        properties = list()
        for member in members:
            if isinstance(member, str):
                properties.append(member)
        with open(configuration_file_location, "r") as file:
            configs = load(file)
        return configs

    @staticmethod
    def save_configurations(target_class, configuration_file_location: str, **kwargs):
        """
        save_configuration will save the configs which has been provided using `**kwargs` parameter.
        `configuration_file_location` parameter's value.
        :param target_class: blueprint of the config.
        :param configuration_file_location: hence the name it requires configuration file location.
        :param kwargs: configs which should meet target_class's blueprint of their attributes.
        :return:
        """
        attributes = ConfigurationHelper.get_class_attributes(target_class)
        configs = dict()
        for key in kwargs:
            if key in attributes:
                configs[key] = kwargs[key]
        with open(configuration_file_location, "w") as file:
            dump(configs, file)

    @staticmethod
    def get_class_attributes(target_class) -> dict:
        """
        get_class_attributes will fetch all the required attributes for the configuration as the name suggests.
        :param target_class: the class which it has the blueprints of attributes.
        :return:
        """
        members = getmembers_static(target_class)
        properties = dict()
        for member, value in members:
            if isinstance(member, str) and member[:2] != "__" and member[-2:] != "__":
                properties[member] = value
        return properties

    def config_singleton(self, target_class, config_class):
        """
        config_singleton will config the target_class based on the config_class configuration
        (static attributes defined in the class).
        Also be aware of the naming for the config_class as in python standard namings you have to name your attributes
        in the pascal-case format but as in for __init__ function you have use snake-case naming convention.
        :param target_class: class for returning instance
        :param config_class: class which has configuration attributes
        :return: target_class which is instantiated with the config
        """
        if self.configuration_file_location is None:
            raise ConfigurationExceptions.ConfigurationFileIsNotInitialized
        try:
            configs = ConfigurationHelper.get_configurations(config_class, self.configuration_file_location)
            sanitized_configs = dict()
            for key in configs:
                name_seperated = re.findall("[A-Z][^A-Z]*", key)
                final_name = ""
                for name in name_seperated:
                    final_name = final_name + name.lower() + "_"
                sanitized_configs[final_name[:-1]] = configs[key]
            return target_class(**sanitized_configs)
        except TypeError as exception:
            # TODO: Add log
            print(exception)
            raise exception
