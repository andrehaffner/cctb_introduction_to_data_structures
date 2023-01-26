from collections import defaultdict
import itertools


class Student:
    id_iter = itertools.count()
    __refs__ = defaultdict(list)

    def __init__(self, name, gender, age, mathematics, physis, chemistry):
        self.id = next(self.id_iter)
        self.name = name
        self.gender = gender,
        self.age = int(age),
        self.mathematics = float(mathematics)
        self.physis = float(physis)
        self.chemistry = float(chemistry)
        self.gpa = (mathematics + physis + chemistry) / 3
