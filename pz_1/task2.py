def world_examination(st):
    l = st.split()
    result = []
    for i in l:
        if i == i[::-1]:
            result.append(i)

    return result


offer = input()
print(world_examination(offer))