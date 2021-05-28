with open('1.txt', mode='r', encoding='UTF-8') as fo:
    for i in fo.readlines():
        print(i)

fo = open('1.txt', mode='r', encoding='UTF-8')
for i in fo.readlines():
    print(i)
fo.close()


class My(object):
    def __init__(self):
        pass

    def __new__(self):
        pass

    def __iter__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __len__(self):
        pass
