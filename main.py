from model.VectorsDB import VectorsDB

def main():
    db = VectorsDB()
    vec = db.get_vector(key = 1)
    print(vec)


if __name__ == '__main__':
    main()