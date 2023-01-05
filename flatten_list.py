# Recursive function that flattens in_list
def flatten_list(in_list):
    if isinstance(in_list, list) is False:
        raise ValueError('Input must be list')

    outer_list = []
    for x in in_list:
        inner_list = []
        if isinstance(x, list):
            inner_list.extend(flatten(x))
        else:
            inner_list.append(x)
        outer_list.extend(inner_list)
    
    return outer_list
