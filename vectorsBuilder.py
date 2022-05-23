from model.WordEmbedding import WordEmbedding
from utils.json_functions import get_data_from_json_file


def get_vertices(json_path):
    js = get_data_from_json_file(json_path)
    vertices = js['vertices']
    return vertices

def VectorsBuilder():
    vertices = get_vertices('./files/hssf.json')
    w = WordEmbedding()
    w.create_table(vertices)
