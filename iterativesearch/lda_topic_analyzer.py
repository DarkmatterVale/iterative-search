import gensim

class LDATopicAnalyzer:

    def __init__(self, logger=None, corpus=None, num_topics=None, dictionary=None, passes=None, workers=None, random_state=None):
        # TODO: Add parameter not null checks here

        self.logger = logger

        self.corpus = corpus
        self.dictionary = dictionary
        self.num_topics = num_topics
        self.passes = passes
        self.workers = workers
        self.random_state = random_state

        self.lda_model = None

        self.is_model_trained = False

    def generate_lda_model(self):
        self.lda_model =  gensim.models.LdaMulticore(
            self.corpus,
            num_topics = self.num_topics,
            id2word = self.dictionary,
            passes = self.passes,
            workers = self.workers,
            random_state = self.random_state)

        self.is_model_trained = True

    def predict_topics(self, doc_bow):
        """
        Predict and return the topics for a document
        """
        # TODO : Add parameter null check here

        self.verify_model_trained()

        return self.lda_model[doc_bow]

    def update_model(self, doc):
        """
        Update the LDA model with the new document
        """
        # TODO : Add parameter null check here
        raise NotImplementedError("TODO: Add update functionality")

    def get_topics(self):
        self.verify_model_trained()

        return self.lda_model.print_topics(-1)

    def log_topics(self):
        for idx, topic in self.get_topics():
            self.logger.info("Topic: {} \nWords: {}".format(idx, topic ))

    def load_lda_model_from_file(self, filename):
        raise NotImplementedError("TODO: Add loading functionality")

    def save_lda_model_to_file(self, filename):
        raise NotImplementedError("TODO: Add saving functionality")

    def verify_model_trained(self):
        if not self.is_model_trained:
            raise ValueError("Cannot get topics of an untrained LDA model")
