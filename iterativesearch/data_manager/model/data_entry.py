import json

class DataEntry:

    def __init__(self, attributes={}):
        self.attributes = attributes

    def set_attribute(self, attribute, value):
        """
        Set an attribute to the specified value.

        :param attribute: Attribute Key
        :type attribute: str
        :param value: Attribute Value
        :type value: str
        """
        self.attributes[attribute] = value

    def get_attribute(self, attribute):
        """
        Returns an attribute. Throws an exception if the attribute does not exist.

        :param attribute: Attribute key
        :type attribute: str
        """
        return self.attributes[attribute]

    def has_attribute(self, attribute):
        """
        Returns True/False if an attribute has been specified.

        :param attribute: Attribute key
        :type attribute: str
        """
        return attribute in self.attributes

    @staticmethod
    def from_json(json_data):
        return DataEntry(json.loads(json_data))

    def to_json(self):
        return json.dumps(self.attributes, sort_keys=True, indent=4)
