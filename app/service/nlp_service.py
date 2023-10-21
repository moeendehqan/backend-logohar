from hazm import *
import os
class sent_vector:
    def __init__(self):
        self.normalizer = Normalizer()
        self.sent2vec_addresse = os.path.join(os.path.join(os.path.dirname(__file__),'nlp_file_models'),'sent2vec-naab.model')
    def normalize_word(self,word):
        return self.normalizer.normalize(word)
    def word_normaloize_and_vector_list(self,word):
        self.sent2vec_model = SentEmbedding(self.sent2vec_addresse)
        word_normal = self.normalize_word(word)
        return self.sent2vec_model[word_normal].tolist()

    