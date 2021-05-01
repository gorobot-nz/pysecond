import pickle


def dumps(obj):
    return pickle.dumps(obj)


def dump(obj, file):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def loads(temp_str):
    return pickle.loads(temp_str)


def load(file):
    with open(file, 'rb') as f:
        result = pickle.load(f)
        return result
