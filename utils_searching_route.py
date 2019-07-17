# Hyun Jin, Jung
# Seoul Nat'l Univ.

import numpy as np
import copy

# quick sort function
def quick_sort(left, right, data):
    pivot = left
    j = pivot
    i = left + 1

    if left < right:
        for k in range(i, right+1):
            if data[k]<data[pivot]:
                j += 1
                data[k], data[j] = data[j], data[k]
        data[left], data[j] = data[j], data[left]
        pivot = j


        quick_sort(left, pivot-1, data)
        quick_sort(pivot+1, right, data)


def pi_multi(left, right, data):
    j = 1
    for i in range(left, right+1):
        j *= data[i]

    return j

def sort_with_tag(row_num, whole_num, data):
    save_data = copy.deepcopy(data)
    quick_sort(0, len(data[0, :])-1, data[row_num, :])
    b_num = []

    i = 0
    while i < len(data[0, :]):
        a = np.where(save_data[row_num, :] == data[row_num, i])
        i = i + len(a[0])
        b_num.extend(a[0])

    for i in b_num:
        for k in np.delete(range(whole_num), row_num):
            data[k, i] = save_data[k, b_num[i]]

    return data

def add_x(route_add, number_plus):
    add_domain = []
    j = 0
    for i in range(len(route_add)):
        k = route_add.index(i)

        if k <= number_plus[0]:
            add_domain.extend([j])
        elif number_plus[0] < k & k <= number_plus[1]:
            j += 1
            add_domain.extend([j])
        else:
            j += 2
            add_domain.extend([j])

    return add_domain
