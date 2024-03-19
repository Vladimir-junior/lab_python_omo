value = input()
count = 0
for i in value:
    count += 1
print('кол буков в слове', count)

p_lower = 0
p_upper = 0
for i in range(1, len(value)):
    if value[i - 1].islower() and value[i].islower():
        p_lower += 1
    if value[i - 1].isupper() and value[i].isupper():
        p_upper += 1
print('верхнего регистра:', p_upper)
print('нижнего регистра:', p_lower)
