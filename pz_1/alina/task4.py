value = input()

point_1 = 'AEIOULNSTR'
point_2 = 'DG'
point_3 = 'BCMP'
point_4 = 'FHVWY'
point_5 = 'K'
point_6 = 'JX'
point_10 = 'QZ'

count = 0

for i in value:
    if i in point_1:
        count += 1
    elif i in point_2:
        count += 2
    elif i in point_3:
        count += 3
    elif i in point_4:
        count += 4
    elif i in point_5:
        count += 5
    elif i in point_6:
        count += 6
    elif i in point_10:
        count += 10

# l = value.upper()
# print(l)
# for i in l:
#     if i in point_1:
#         count += 1
#     elif i in point_2:
#         count += 2
#     elif i in point_3:
#         count += 3
#     elif i in point_4:
#         count += 4
#     elif i in point_5:
#         count += 5
#     elif i in point_6:
#         count += 6
#     elif i in point_10:
#         count += 10

print(count)