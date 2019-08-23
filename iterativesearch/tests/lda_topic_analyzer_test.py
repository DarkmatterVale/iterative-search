from sklearn.datasets import fetch_20newsgroups
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
import unittest
from ..lda_builder import LDABuilder
from loguru import logger
import os

class LDATopicAnalyzerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.newsgroups_train = fetch_20newsgroups(subset="train", shuffle = False)
        cls.newsgroups_test = fetch_20newsgroups(subset="test", shuffle = False)

        nltk.download('wordnet')

        cls.processed_docs = []
        for doc in cls.newsgroups_train.data:
            cls.processed_docs.append(cls.preprocess(doc))

        cls.dictionary = gensim.corpora.Dictionary(cls.processed_docs)
        cls.dictionary.filter_extremes(no_below=15, no_above=0.1, keep_n= 100000)
        cls.bow_corpus = [cls.dictionary.doc2bow(doc) for doc in cls.processed_docs]

        cls.builder = LDABuilder(logger)
        cls.builder.set_num_topics(10).set_passes(5).set_workers(4).set_random_state(1).set_dictionary(cls.dictionary).set_corpus(cls.bow_corpus)

        cls.lda_topic_analyzer = cls.builder.build()
        cls.lda_topic_analyzer.train_model()

    @classmethod
    def tearDownClass(cls):
        for file in os.listdir("."):
            if "tmp" in file:
                os.remove(file)

    def test_builder_construction_pass(self):
        num_topics = 10
        passes = 5
        workers = 4
        random_state = 420
        dictionary = {}
        corpus = {}

        builder = LDABuilder(logger)
        builder.set_num_topics(num_topics).set_passes(passes).set_workers(workers).set_random_state(random_state).set_dictionary(dictionary).set_corpus(corpus)
        lda_topic_analyzer = builder.build()

        self.assertEqual(lda_topic_analyzer.num_topics, num_topics)
        self.assertEqual(lda_topic_analyzer.passes, passes)
        self.assertEqual(lda_topic_analyzer.workers, workers)
        self.assertEqual(lda_topic_analyzer.dictionary, dictionary)
        self.assertEqual(lda_topic_analyzer.corpus, corpus)
        self.assertEqual(lda_topic_analyzer.random_state, random_state)

    @classmethod
    def lemmatize_stemming(cls, text):
        return SnowballStemmer("english").stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    @classmethod
    def preprocess(cls, text):
        result=[]
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                result.append(cls.lemmatize_stemming(token))

        return result

    def test_lda_topic_analyzer_function(self):
        self.assertIsNotNone(self.lda_topic_analyzer.get_topics())

    def test_lda_topic_analyzer_prediction(self):
        self.assertIsNotNone(self.lda_topic_analyzer.predict_topics(self.bow_corpus[1]))

    def test_lda_model_save_pass(self):
        self.assertFalse(os.path.exists("tmp.lda"))
        self.lda_topic_analyzer.save_model("tmp.lda")
        self.assertTrue(os.path.exists("tmp.lda"))

        new_lda_topic_analyzer = self.builder.build()

        self.assertFalse(new_lda_topic_analyzer.is_model_trained)
        new_lda_topic_analyzer.load_model("tmp.lda")
        self.assertTrue(new_lda_topic_analyzer.is_model_trained)

        self.assertIsNotNone(new_lda_topic_analyzer.predict_topics(self.bow_corpus[1]))
