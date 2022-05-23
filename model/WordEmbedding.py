import string
import fasttext as fasttext
from model.VectorsDB import VectorsDB


class WordEmbedding:

    def __init__(self, project_name = 'poi'):
        self.project_name = project_name
        self.db = VectorsDB()
        # self.db.create_table(project_name)
        # self.load_model()
        # self.create_table()

    def load_model(self):
        print("loading model")
        self.model = fasttext.load_model('./model/cc.en.300.bin')

    def create_table(self, vertices):
        for vertex in vertices:
            key = vertex['key']
            name = vertex['name']
            vector = self.model[name]
            self.db.insert_vector(self.project_name, key, vector)

    def get_vector(self, key:int):
        return self.db.get_vector(self.project_name, key)



