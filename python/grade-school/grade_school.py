class School(object):
    def __init__(self, school_name):
        self.name = school_name
        self.items = [tuple()]*9

    def add(self, student_name, grade):
        prev = list(self.items[grade-1])
        prev.append(student_name)
        self.items[grade-1] = tuple(prev)

    def grade(self, grade):
        return sorted(self.items[grade-1])

    def sort(self):
        sorted(self.items, key=len)
        tmp = []
        for g, tup in enumerate(self.items):
            tmptuple = (g+1, tup)
            if tup == ():
                continue
            tmp.append(tmptuple)
        return tmp
