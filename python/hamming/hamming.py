def distance(init, new):
    if len(init) != len(new):
        raise ValueError
    i = 0
    for init_ele, new_ele in zip(init, new):
        if init_ele != new_ele:
            i += 1
    return i
