def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
            return min
        print("smallest number", smallest_num_in_list([1, 2, -8, 0]))
