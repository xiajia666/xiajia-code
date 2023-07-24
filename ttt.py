world = "python"
list = []
for i in world:
    list.append(i)
print(list)
print(list[3])
finall_4 = [list[i] for i in range((len(list) - 4),(len(list)))]
print(finall_4)