def flatten(in_list):
    if isinstance(in_list, list):
        outer_list = []
        for x in in_list:
            inner_list = []
            if isinstance(x, list):
                inner_list.extend(flatten(x))
            else:
                inner_list.append(x)
            outer_list.extend(inner_list)
        return outer_list
    else:
        return in_list
