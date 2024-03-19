l = [-2, -4, 3, 5, 0, 2, 2, 0, 6]
result = 0
for i in l:
    if i < 0:
        result += i
print('sum otr = ', result)
result_0 = 0
zero_element_index = [i for i, x in enumerate(l) if x == 0]
if len(zero_element_index) < 2:
    result_0 = 0
else:
    product_zero_number = 0
    product_list = l[zero_element_index[0]:zero_element_index[1]]
    product_list.pop(0)
    for i in product_list:
        product_zero_number += i

print("sum mezdu nulami", product_zero_number)