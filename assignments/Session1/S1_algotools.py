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
        elif item==0:
            print('This value is null : ' + str(item))
        else:
            print('This value is negative : ' + str(item))
    moy = float(positive_value_sum) / float(positive_value_count)

    return moy


my_list = [1, 2, 3, 4, -7]

result = average_above_zero(my_list)
message = "The average of positive samples of {list_values} is {res}" .format(list_values=my_list, res=result)
print(message)
