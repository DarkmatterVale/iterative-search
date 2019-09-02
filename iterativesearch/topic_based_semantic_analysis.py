class TopicBasedSemanticAnalysis:

    DEFAULT_TOPIC_SCORE = 0
    DEFAULT_DOCUMENT_SCORE = 0

    def __init__(self, topics={}):
        """
        :param topics: Initial topics (& scores)
        :type topics: dict(key: str value: int)
        """
        self.topics = topics

    def reset_topics(self):
        """
        Resets the topics.
        """
        self.topics = {}

    def score_document(self, document_topics):
        """
        Score a document on its search relevance based on topics.

        :param document_topics: Topics contained within the document
        :type document_topics: list(str)
        """
        score = TopicBasedSemanticAnalysis.DEFAULT_DOCUMENT_SCORE

        for topic in document_topics:
            if self.is_topic_score_specified(topic):
                score += self.topics[topic]

        return score

    def update_topic_score(self, topic, score_delta):
        """
        Update the relevancy score associated with a topic.

        :param topic: Topic to update
        :type topic: str
        :param score_delta: Change in score of topic
        :type score_delta: int
        """
        if not self.is_topic_score_specified(topic):
            self.topics[topic] = TopicBasedSemanticAnalysis.DEFAULT_TOPIC_SCORE

        self.topics[topic] += score_delta

    def get_topic_score(self, topic):
        """
        Returns the topic score if set up. Otherwise, returns the default topic score.
        """
        if self.is_topic_score_specified(topic):
            return self.topics[topic]

        return TopicBasedSemanticAnalysis.DEFAULT_TOPIC_SCORE

    def is_topic_score_specified(self, topic):
        """
        Returns True/False whether or not a topic has already had a score assigned to it.

        :param topic: Topic to look at
        :type topic: str
        """
        return topic in self.topics
