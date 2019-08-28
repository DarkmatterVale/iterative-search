from abc import abstractmethod

class DataProcessor:

    @abstractmethod
    def process(self, raw_data, **kwargs):
        """
        Processes raw data, returning the processed data.

        :param raw_data: Raw data to process
        :type raw_data: Specific to implementation
        :return: Processed data. Type specific to implementation
        """
        raise NotImplementedError("process() not implemented")
