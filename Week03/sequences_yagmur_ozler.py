def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    my_set = set(seq)
    my_seq = list(my_set)
    return my_seq


def list_counts(seq: list) -> dict:
    """
    This function counts the number of 
    occurrences of each item in a list.
    """
    my_dict = {}
    for num in seq:
        num_count = seq.count(num)
        my_dict[num] = num_count
    return my_dict

def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys 
    and values of a dictionary.
    """

    reversed_dict = {}
    
    for key, value in d.items():
        reversed_dict[value] = key

    return reversed_dict
