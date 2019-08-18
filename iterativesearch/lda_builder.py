from .lda_topic_analyzer import LDATopicAnalyzer

class LDABuilder:

    def __init__(self, logger):
        self.logger = logger

        self.num_topics = None
        self.passes = None
        self.workers = None
        self.random_state = None

        self.dictionary = None
        self.corpus = None

    def build(self):
        return LDATopicAnalyzer(
            logger = self.logger,
            dictionary = self.dictionary,
            corpus = self.corpus,
            num_topics = self.num_topics,
            passes = self.passes,
            workers = self.workers,
            random_state = self.random_state)

    def set_num_topics(self, num_topics):
        """
        :param num_topics: number of topics
        :type num_topics: int
        """
        self.num_topics = num_topics

        return self

    def set_passes(self, passes):
        """
        :param passes: number of passes to train LDA model
        :type passes: int
        """
        self.passes = passes

        return self

    def set_workers(self, workers):
        """
        :param workers: number of workers to train LDA model
        :type workers: int
        """
        self.workers = workers

        return self

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

        return self

    def set_corpus(self, corpus):
        self.corpus = corpus

        return self

    def set_random_state(self, random_state):
        self.random_state = random_state

        return self
