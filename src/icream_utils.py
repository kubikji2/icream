from random import randint

# based on:
# https://www.geeksforgeeks.org/python-get-unique-values-list/
# function to get unique values
def unique1(non_unique_list):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in non_unique_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list


# based on:
# https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# function to get unique values
def unique2(non_unique_list):
    return list(set(non_unique_list))

# based on:
# https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# function to get unique values
def unique3(non_unique_list):

    _set = set()
     
    # traverse for all elements
    for x in non_unique_list:
        _set.add(x)     
    return list(_set)

# function to get unique values
# '-> based on: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# '-> NOTE: fastest from considered options
def unique(non_unique_list):
    return list(set(non_unique_list))

if __name__=="__main__":
    import time

    _l = []
    for i in range(1000):
        _l.append(randint(0,100))
    
    uniques = [unique1,unique2,unique3]
    for i in range(3):
        unique = uniques[i]
        _start = time.time()
        a = unique(_l)
        _end = time.time()
        _elapsed = _end - _start
        print("fcn {} elapsed: {}".format(i, _elapsed))