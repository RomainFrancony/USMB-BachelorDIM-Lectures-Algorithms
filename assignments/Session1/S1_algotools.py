##
# @author : Romain Francony, IT Student
# brief : a set of generic functions for data managements


def average_above_zero(input_list):
    ##
    # Get average of positive number in a list
    # @param input_list : the list to be scanned
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

    if positive_value_count == 0:
        return 0

    moy = float(positive_value_sum) / float(positive_value_count)
    return moy


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

    if len(list_x) == 0 or len(list_y) == 0:
        raise ValueError("The matrix is empty")

    a = b = c = d = 0
    a = min(list_x)
    b = min(list_y)
    c = max(list_x)
    d = max(list_y)
    return numpy.array([[a, b], [a, d], [c, b], [c, d]])


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


def remove_whitespace(table):
    ##
    # Remove space from string
    # @param table : the string you want to remove space from
    return table.replace(" ", "")


"""
message = ' hello world '
my_table_nospace = remove_whitespace(message)
print 'The initial message : {message}'.format(message=message)
print 'the message without space : {new_table}'.format(new_table=my_table_nospace)
"""

from random import randint


def shuffle(list):
    ##
    # Shuffle a list of items
    # @param list : the list of items you want to shuffle
    copy = list[:]
    new_list = []
    length = len(copy)
    for i in range(length):
        index = randint(0, len(copy) - 1)
        new_list.append(copy[index])
        del copy[index]

    return new_list


"""
list = [1, 2, 3, 4, 5, 6]
list_shuffle = shuffle(list)
print 'Old list : {list}'.format(list=list)
print 'New list : {list}'.format(list=list_shuffle)
"""

"""
Selective Sort
a)
10, 15, 7, 1, 3, 3, 9
We start iterating over the vector
1 is the minimum, we swap 10 and 1 and restart but from index 1

the vector is now : 1, 15, 7, 10, 3, 3, 9
3 is the minimum, we swap 15 and 3 and restart from index 2

the vector is now : 1, 3, 7, 10, 15, 3, 9
3 is the minimum, we swap 7 and 3 and restart from index 3

the vector is now : 1, 3, 3, 10, 15, 7, 9
7 is the minimum, we swap 10 and 7 and restart from index 4

the vector is now : 1, 3, 3, 7, 15, 10, 9
9 is the minimum, we swap 15 and 9 and restart from index 5

we now have 1, 3, 3, 7, 9, 10, 15

the last iteration doesn't change anything since the numbers are already in the right order

we've iterated over the whole vector so it's now sorted

b) No the number of iterations depend of the length of the vector, it will always do n-1 iterations

c) we need 6 (n-1) iterations for sorting the whole vector (even if the're numbers already in the right index

d) 5 permutations were applied (no permutation needed during the last iterations since the number were already in the right order)

e) 7(7-1)/2 = 21 So 21 comparisons are applied

f) The complexity of this algorithm is O(n^2)

g) In the worst case of vector, we have
n = 50 : (n-1) 49 permutations, 50(50-1)/2 = 1225 comparisons
n = 100 : (n-1) 99 permutations, 100(100-1)/2 = 4950 comparisons
n = 500 : (n-1) 499 permutations, 500(500-1)/2 = 124750 comparisons
"""


def sort_selective(list_in):
    ##
    # Sort selective function
    # @param list_in : the list to sort
    for i in xrange(len(list_in) - 1):
        min_index = i
        for j in xrange(i, len(list_in)):
            if list_in[j] < list_in[min_index]:
                min_index = j

        if min_index != i:
            swap = list_in[min_index]
            list_in[min_index] = list_in[i]
            list_in[i] = swap

    return list_in


"""
list = [10, 15, 7, 1, 3, 3, 9]
print 'List before sort : {list}'.format(list=list)

sorted_list = sort_selective(list)
print 'List after sort : {list}'.format(list=sorted_list)
"""

"""
Bubble Sort
a) 
10, 15, 7, 1, 3, 3, 9
we swap 15 and 7
10, 7, 15, 1, 3, 3, 9
we swap 15 and 1
10, 7, 1, 15, 3, 3, 9
we swap 15 and 3
10, 7, 1, 3, 15, 3, 9
we sap 15 and 3
10, 7, 1, 3, 3, 15, 9
we swap 15 and 9
10, 7, 1, 3, 3, 9, 15

We restart from the beginning
we swap 10 and 7
7, 10, 1, 3, 3, 9, 15
we swap 10 and 1
7, 1, 10, 3, 3, 9, 15
we swap 10 and 3
7, 1, 3, 10, 3, 9, 15
we swap 10 and 3
7, 1, 3, 3, 10, 9, 15
we swap 10 and 9
7, 1, 3, 3, 9, 10, 15

We restart from the beginning
we swap 7 and 1
1, 7, 3, 3, 9, 10, 15
we swap 7 and 3
1, 3, 7, 3, 9, 10, 15
we swap 7 and 3
1, 3, 3, 7, 9, 10, 15

No permutations needed, the vector is sorted


b) Yes the number of iterations depend on the vector content

c) 3 iterations are needed to sort the vector

d) 13 permutations are applied

e) 21 comparisons are applied

f) The complexity of this algorithm is O(n^2)

g) In the worst case, we have
n = 50 : 1225-50 = 1175 permutations, 50(50-1)/2 = 1225 comparisons
n = 100 : 4950 - 100 = 4850 permutations, 100(100-1)/2 = 4950 comparisons
n = 500 : 124750 - 500 = 124250 permutations, 500(500-1)/2 = 124750 comparisons
"""


def sort_bubble(list_in):
    ##
    # Bubble selective function
    # @param list_in : the list to sort
    for i in xrange(0, len(list_in) - 1):
        for j in xrange(0, len(list_in) - 1):
            if list_in[j] > list_in[j + 1]:
                swap = list_in[j + 1]
                list_in[j + 1] = list_in[j]
                list_in[j] = swap

    return list_in


"""
list = [10, 15, 7, 1, 3, 3, 9]
print 'List before sort : {list}'.format(list=list)

sorted_list = sort_bubble(list)
print 'List after sort : {list}'.format(list=sorted_list)
"""
