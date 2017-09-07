##
# @author : Romain Francony, IT Student
# brief : a set of generic functions for data managements


def average_above_zero(input_list):
    positive_value_sum = 0
    positive_value_count = 0

    # loop over the items of the list
    for item in input_list:
        # select only positive items
        if item > 0:
            positive_value_sum += item
            positive_value_count += 1
        elif item == 0:
            print('This value is null : ' + str(item))
        else:
            print('This value is negative : ' + str(item))
    moy = float(positive_value_sum) / float(positive_value_count)

    return moy


""" #testing average above zero function
my_list = [1, 2, 3, 4, -7]

result = average_above_zero(my_list)
message = "The average of positive samples of {list_values} is {res}" .format(list_values=my_list, res=result)
print(message)
"""


def max_value(list):
    ##
    # Basic function able to return the max value of a list
    # @param list : the list to be scanned
    # @throws a exception (ValueError) on an empty list

    # Throw exception if the list is empty
    if len(list) == 0:
        raise ValueError("The list is empty")

    max = list[0]
    index_of_max = 0
    for index, item in enumerate(list):
        if item > max:
            max = item
            index_of_max = index
    return max, index_of_max


"""# testing max_value function
my_list = [1, 2, 3, 4, -7]
result = max_value(my_list)
message = "The max value of {list_values} is : {res} at index : {res_index}".format(list_values=my_list, res=result[0], res_index=result[1])
print(message)
"""


def reverse_table(list):
    ##
    # Basic function able to reverse a list
    # @param list : the list to be scanned
    # @throws a exception (ValueError) on an empty list

    list_size = len(list)
    # Throw exception if the list is empty
    if list_size == 0:
        raise ValueError("The list is empty")

    # loop through the first half of the list and inverse his position
    for index in xrange(list_size / 2):
        saved_value = list[list_size - index - 1]
        list[list_size - index - 1] = list[index]
        list[index] = saved_value

    return list


"""# testing reverse_table function
my_list = [1, 2, 3, 4, -7]
# keep the initial list in str because we change it in the function
initial_list = str(my_list)
result = reverse_table(my_list)
message = "The reverse value of {list_values} is : {res}".format(list_values=initial_list, res=result)
print(message)
"""
