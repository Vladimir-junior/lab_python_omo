num = input()
cet = 0
ne_cet = 0
for i in num:
    if int(i) % 2 == 0:
        cet += 1
    else:
        ne_cet += 1

print(f"cet = {cet}, necet = {ne_cet}")
