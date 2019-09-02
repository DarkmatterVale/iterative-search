import unittest
from ..topic_based_semantic_analysis import TopicBasedSemanticAnalysis

class TopicBasedSemanticAnalysisTestCase(unittest.TestCase):

    def test_is_topic_score_specified_pass_1(self):
        semantic_analysis = TopicBasedSemanticAnalysis()

        self.assertFalse(semantic_analysis.is_topic_score_specified("test_topic_1"))

    def test_is_topic_score_specified_pass_2(self):
        semantic_analysis = TopicBasedSemanticAnalysis()

        self.assertFalse(semantic_analysis.is_topic_score_specified("test_topic_2"))

    def test_is_topic_score_specified_pass_3(self):
        semantic_analysis = TopicBasedSemanticAnalysis()

        semantic_analysis.update_topic_score("test_topic_3", 1)

        self.assertTrue(semantic_analysis.is_topic_score_specified("test_topic_3"))

    def test_get_topic_score_pass_1(self):
        semantic_analysis = TopicBasedSemanticAnalysis()

        semantic_analysis.update_topic_score("test_topic_3", 1)

        self.assertEqual(1, semantic_analysis.get_topic_score("test_topic_3"))

    def test_get_topic_score_pass_2(self):
        semantic_analysis = TopicBasedSemanticAnalysis()
        semantic_analysis.update_topic_score("test_topic_3", 1)

        self.assertEqual(TopicBasedSemanticAnalysis.DEFAULT_TOPIC_SCORE, semantic_analysis.get_topic_score("test_topic_2"))

    def test_reset_topics(self):
        semantic_analysis = TopicBasedSemanticAnalysis()

        semantic_analysis.update_topic_score("test_topic_11", 1)
        semantic_analysis.reset_topics()

        self.assertEqual(TopicBasedSemanticAnalysis.DEFAULT_TOPIC_SCORE, semantic_analysis.get_topic_score("test_topic_11"))

    def test_update_topic_score_pass_1(self):
        semantic_analysis = TopicBasedSemanticAnalysis()
        semantic_analysis.reset_topics()

        semantic_analysis.update_topic_score("test_topic_5", 1)

        self.assertEqual(semantic_analysis.get_topic_score("test_topic_5"), 1)

    def test_score_document_pass_1(self):
        semantic_analysis = TopicBasedSemanticAnalysis()
        semantic_analysis.reset_topics()

        semantic_analysis.update_topic_score("test_topic_1", 5)
        semantic_analysis.update_topic_score("test_topic_3", -3)
        semantic_analysis.update_topic_score("test_topic_11", -4)

        document = ["test_topic_1", "test_topic_3", "test_topic_11"]

        self.assertEqual(semantic_analysis.score_document(document), -2)
