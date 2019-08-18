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

class LDATopicAnalyzerTestCase(unittest.TestCase):

    # TODO : Add tests to verify non-null parameters

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

    def lemmatize_stemming(self, text):
        return SnowballStemmer("english").stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    # Tokenize and lemmatize
    def preprocess(self, text):
        result=[]
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                result.append(self.lemmatize_stemming(token))

        return result

    def test_lda_topic_analyzer_function(self):
        newsgroups_train = fetch_20newsgroups(subset="train", shuffle = False)
        newsgroups_test = fetch_20newsgroups(subset="test", shuffle = False)

        nltk.download('wordnet')

        processed_docs = []
        for doc in newsgroups_train.data:
            processed_docs.append(self.preprocess(doc))

        dictionary = gensim.corpora.Dictionary(processed_docs)
        dictionary.filter_extremes(no_below=15, no_above=0.1, keep_n= 100000)
        bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

        builder = LDABuilder(logger)
        builder.set_num_topics(10).set_passes(5).set_workers(4).set_random_state(1).set_dictionary(dictionary).set_corpus(bow_corpus)

        lda_topic_analyzer = builder.build()
        lda_topic_analyzer.generate_lda_model()

        self.assertIsNotNone(lda_topic_analyzer.get_topics())
