# Hyun Jin, Jung
# Seoul Nat'l Univ.
# @Copyright

import numpy as np
import matplotlib.pyplot as plt
import utils_searching_route as ut
import copy

### input informations of searching route
# variable
column_num = 200

# non-variable
np.random.seed(19)
vari_prob = np.round(np.random.rand(3, column_num), 4)
number_plus = [int(column_num/2) - 1, column_num - 1]
route_add = []
sort_vari_prob = np.empty((3, column_num))

### generate probability
vari_prob[2, range(1, column_num, 2)] = 0
for i in range(column_num):
    vari_prob[:, i] = np.divide(vari_prob[:, i], np.float(vari_prob[0, i]+vari_prob[1, i]+vari_prob[2, i]))
sort_vari_prob = copy.deepcopy(vari_prob)

### modulate
# sorting
sort_vari_prob = ut.sort_with_tag(2, 3, sort_vari_prob)
sprt_vari_prob = ut.sort_with_tag(1, 3, sort_vari_prob[:, 0:int(column_num/2)])

# compare and set number of value
j = int(column_num/2)
while j>0:
    j -= 2
    comp_num_left = ut.pi_multi(0, number_plus[0], sort_vari_prob[0, :]) * ut.pi_multi(number_plus[0] + 1, number_plus[1], sort_vari_prob[1, :]) * ut.pi_multi(number_plus[1] + 1, column_num - 1, sort_vari_prob[2, :])
    i = 1
    while 2 * i + 1 <= number_plus[1] - number_plus[0]:
        comp_num_right = ut.pi_multi(0, number_plus[0] + i, sort_vari_prob[0]) * ut.pi_multi(number_plus[0] + i + 1, number_plus[1] - i, sort_vari_prob[1]) * ut.pi_multi(number_plus[1] - i + 1, column_num - 1, sort_vari_prob[2])
        if comp_num_left <= comp_num_right:
            number_plus[0] += i
            number_plus[1] -= i
            break
        else:
            i += 1

print(number_plus)


# set route
for i in range(column_num):
    if i <= number_plus[0]:
        a = np.where(vari_prob[0, :] == sort_vari_prob[0, i])
        route_add.extend(a[0])
        i = i + len(a[0]) - 1
    elif number_plus[0] < i & i <= number_plus[1]:
        a = np.where(vari_prob[1, :] == sort_vari_prob[1, i])
        route_add.extend(a[0])
        i = i + len(a[0]) - 1
    else:
        a = np.where(vari_prob[2, :] == sort_vari_prob[2, i])
        route_add.extend(a[0])
        i = i + len(a[0]) - 1
print(route_add)
u = ut.add_x(route_add, number_plus)
u.insert(0, 0)

# plot
plt.plot()
plt.plot(range(column_num+1), u)
plt.savefig(r'C:\Users\Owner\marg_file\route_searching_save\fig_' + str(vari_prob[0, 0]) + '.jpg')


