class Sun(object):

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


p = Sun.instance()
f = Sun.instance()
try:
    a = Sun()
except Exception as e:
    print(e)
print(p is f)
