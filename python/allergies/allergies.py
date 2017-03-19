from collections import OrderedDict


d = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}

ALLERGIES_D_S = OrderedDict(reversed(sorted(d.items(), key=lambda t: t[1])))


class Allergies(object):
    def __init__(self, score):
        self.score = score % 256
        self.lst = []
        base_value = self.score
        for k, value in ALLERGIES_D_S.items():
            if base_value >= value:
                print("Adding ", k, "of value", value)
                self.lst.append(k)
                base_value -= value

    def is_allergic_to(self, arg):
        return arg in self.lst
