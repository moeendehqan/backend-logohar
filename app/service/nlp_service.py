

from hazm import *
import os

class sent_vector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(sent_vector, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.normalizer = Normalizer()
        self.sent2vec_addresse = os.path.join(os.path.join(os.path.dirname(__file__),'nlp_file_models'),'sent2vec-naab.model')
        self.sent2vec_model = SentEmbedding(self.sent2vec_addresse)

    def normalize_word(self, word):
        return self.normalizer.normalize(word)

    def word_normaloize_and_vector_list(self, word):
        word_normal = self.normalize_word(word)
        return self.sent2vec_model[word_normal].tolist()
