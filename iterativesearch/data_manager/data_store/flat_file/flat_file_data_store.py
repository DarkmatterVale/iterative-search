from ..data_store import DataStore
from ...model import DataEntry
import os
import json
import shutil

class FlatFileDataStore(DataStore):

    def __init__(self, path=""):
        self.path = path

    def initialize(self, **kwargs):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        self.update_data_store_size()

    def get_all_data(self):
        data = []

        for file in os.listdir(self.path):
            with open(os.path.join(self.path, file), 'r') as json_file:
                data_json = json.load(json_file)

                data.append(DataEntry.from_json(data_json))

        return data

    def add_data(self, data):
        json_data = data.to_json()

        save_path = self.get_save_path()

        with open(save_path, "w") as json_file:
            json.dump(json_data, json_file)

            self.update_data_store_size()

    def query(self, query_parameters):
        raise NotImplementedError("query() not implemented")

    def clear_all_data(self):
        shutil.rmtree(self.path)

        self.initialize()

    def get_save_path(self):
        """
        Returns the path
        """
        return os.path.join(self.path, str(self.data_store_size + 1))

    def update_data_store_size(self):
        """
        Updates internal tracker to keep track of how many data elements exist.
        """
        self.data_store_size = len(os.listdir(self.path))
