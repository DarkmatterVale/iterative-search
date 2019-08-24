from abc import abstractmethod

class DataProcessor:

    def process(self, raw_data, **kwargs):
        """
        Processes raw data, returning the processed data.

        :param raw_data: Raw data to process
        :type raw_data: RawSearchResultData
        :return: ProcessedWarehouseData
        """
        raise NotImplementedError("process() not implemented")
