from abc import abstractmethod

class TopicAnalyzer:

    @abstractmethod
    def train_model(self):
        """
        Train a model
        """
        raise NotImplementedError("train_model() not implemented")

    @abstractmethod
    def predict_topics(self, doc_bow):
        """
        Predict and return the topics for a document

        :param doc_bow: document in BOW format, generated from the dictionary passed into the object
        :type doc_bow: BOW
        """
        raise NotImplementedError("predict_topics() not implemented")

    @abstractmethod
    def get_topics(self):
        """
        Returns the topics generated by the model
        """
        raise NotImplementedError("get_topics() not implemented")

    @abstractmethod
    def log_topics(self):
        """
        Logs the topics generated by the model to the logger
        """
        raise NotImplementedError("log_topics() not implemented")

    @abstractmethod
    def load_model(self, filename):
        """
        Load a model from flat-file storage

        :param filename: Model filename
        :type filename: str
        """
        raise NotImplementedError("load_model() not implemented")

    @abstractmethod
    def save_model(self, filename):
        """
        Save a model to flat-file storage

        :param filename: filename for model to be stored in
        :type filename: str
        """
        raise NotImplementedError("save_model() not implemented")