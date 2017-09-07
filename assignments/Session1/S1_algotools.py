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

import numpy


def roi_bbox(image_matrix):
    ##
    # Basic function able to get bounding box of an image matrix
    # @param image_matrix : the image matrix
    list_x = []
    list_y = []

    rows_length = image_matrix.shape[0]
    cols_length = image_matrix.shape[1]

    # search all colored pixel
    for row in xrange(rows_length):
        for col in xrange(cols_length):
            if image_matrix[row][col] == 1:
                list_x.append(row)
                list_y.append(col)

    a = b = c = d = 0
    a = min(list_x)
    b = min(list_y)
    c = max(list_x)
    d = max(list_y)
    return numpy.array([[a, b], [a, d], [c, b], [c, d]])


"""
size_rows = 10
size_cols = 10
my_matrix = numpy.zeros([size_rows, size_cols], bool)
my_matrix[3:4, 6:9] = numpy.ones([1, 3])
my_matrix[2:4, 6:8] = numpy.ones([2, 2])

result = roi_bbox(my_matrix)
message = "The coordinates of the image's bounding box are : {result}" .format(result=result)
print(message)
"""
import random


def random_fill_sparse(table, vfill):
    ##
    # Basic function able tto fill a table
    # @param table : the table
    # @params vfill : number of item to fill
    if table.shape[0] != table.shape[1]:
        raise ValueError("The table is not square")

    table_size = len(table) - 1
    for i in range(vfill):
        filled = False
        while not (filled):
            alea_x = random.randint(0, table_size)
            alea_y = random.randint(0, table_size)
            if table[alea_x][alea_y] == '':
                table[alea_x][alea_y] = 'X'
                filled = True

    return table


"""
my_table = numpy.full([5, 5], '', dtype=str)
fill = 5
filled_table = random_fill_sparse(my_table, fill)
message = 'The table with {fill} X'.format(fill=fill)
print(message)
print(filled_table)
"""
