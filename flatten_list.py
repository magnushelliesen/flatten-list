# Recursive function that flattens arbitrarily nested in_list
def flatten_list(input_list):
    if isinstance(input_list, list) is False:
        raise ValueError('Input must be list')

    outer_list = []
    for element in input_list:
        inner_list = []
        if isinstance(element, list):
            inner_list.extend(flatten_list(element))
        else:
            inner_list.append(element)
        outer_list.extend(inner_list)

    return outer_list