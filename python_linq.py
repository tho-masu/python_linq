import copy

# python向けC#LINQ風ライブラリ(自作)
# ミュータブル(変更可能)オブジェクトだが、コンストラクタ実行時にcopy.deepcopy()される

class Enumerable:
    __lst: list = None

    def __init__(self, obj) -> None:
        if isinstance(obj, list) or isinstance(obj, tuple):
            self.__lst = list(copy.deepcopy(obj))
        else:
            raise TypeError('■ WARNING: Object is not list or tuple.')

    def print(self) -> None:
        print(self.__lst)

    def get(self) -> list:
        return self.__lst

    def toList(self) -> list:
        return self.__lst

    def toTuple(self) -> tuple:
        return tuple(self.__lst)

    def toSet(self) -> set:
        return set(self.__lst)

    def toDict(self, callback) -> dict:
        return {callback(item): item for item in self.__lst}

    def select(self, callback):
        self.__lst = [callback(item) for item in self.__lst]
        return self

    def where(self, callback):
        self.__lst = [item for item in self.__lst if callback(item)]
        return self

    def take(self, n: int):
        self.__lst = self.__lst[:n]
        return self

    def takeFromTo(self, f: int, t: int):
        self.__lst = self.__lst[f-1:t]
        return self

    def skip(self, n: int):
        self.__lst = self.__lst[n:]
        return self

    def first(self):
        return self.__lst[0]

    def firstCall(self, callback):
        for item in self.__lst:
            if callback(item):
                return item
        return None

    def last(self):
        return self.__lst[len(self.__lst)-1]

    def lastCall(self, callback):
        for item in reversed(self.__lst):
            if callback(item):
                return item
        return None

    def distinct(self):
        self.__lst = list(set(self.__lst))
        return self

    def count(self) -> int:
        return len(self.__lst)

    def countCall(self, callback) -> int:
        i = 0
        for item in self.__lst:
            if callback(item):
                i += 1
        return i

    def any(self, callback) -> bool:
        flag = False
        for item in self.__lst:
            if callback(item):
                flag = True
        return flag

    def all(self, callback) -> bool:
        flag = True
        for item in self.__lst:
            if not callback(item):
                flag = False
        return flag

    def orderBy(self, callback):
        self.__lst.sort(key=callback)
        return self

    def reverse(self):
        self.__lst.reverse()
        return self

    def merge(self, enumerable):
        return Enumerable(self.__lst + enumerable.toList())

    def deepcopy(self):
        return copy.deepcopy(self)
