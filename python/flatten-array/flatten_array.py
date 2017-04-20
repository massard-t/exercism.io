from collections import Sequence


def subf(current_array, tmp):
    if isinstance(tmp, Sequence):
        print(tmp)
        for ele in tmp:
            if isinstance(ele, str):
                current_array.append(tmp)
                continue
            subf(current_array, ele)
    elif tmp is not None:
        #if isinstance(tmp, Sequence):

        print(tmp)
        current_array.append(tmp)

def flatten(array):
    tmp = []
    for ele in array:
        subf(tmp, ele)
    return tmp
