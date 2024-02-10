def sum_number(num):
    num_st = str(num)
    d = list(num_st)
    result = 0
    for i in d:
        result += int(i)

    return result


number = int(input())
print(sum_number(number))