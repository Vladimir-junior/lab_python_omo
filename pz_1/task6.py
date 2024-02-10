from random import randint

l = []

for i in range(10):
    l.append(randint(1, 100))

tp = tuple(l)
print(tp)
print(max(tp))
print(min(tp))



# способ 2
# tp_1 = (34,76,32,5,76)
# tp_2 = (78,53,4,98,23)
# tp = tp_1 + tp_2
# print(tp)
# print(max(tp))
# print(min(tp))


