# Recursive function that flattens arbitrarily nested input_list
def flatten_list(input_list):
    if (isinstance(input_list, list) or isinstance(input_list, tuple)) is False:
        raise ValueError('Input must be list')

    outer_list = []
    for element in input_list:
        inner_list = []
        if isinstance(element, list) or isinstance(element, tuple):
            inner_list.extend(flatten_list(element))
        else:
            inner_list.append(element)
        outer_list.extend(inner_list)

    return outer_list