from random import randint

l = tuple(randint(1,100) for _ in range(10))

print(l)
print(max(l))
print(min(l))



