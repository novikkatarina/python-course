# lst = [i for i in range(10)]
# lst2 = [i for i in range(10, 20)]
#print(lst)
#print(lst2)

# str = 'abdefgh'
# for i, ch in enumerate(str):
#     print(ch, i)

#enumeration = [i for i in range(len(str))]
#for pair in zip(str, enumeration):
#    print(pair)
   

#for pair in zip(lst, lst2):
#    print(pair)

#print(list(map(lambda x: x * -1, lst)))

# filtered = filter(lambda x: x > 5, lst)
# lst = list(filtered)
# print(lst)

lst1 = [0, 1, 2]
lst2 = [1, 2, 3]
res = []


# for x1, x2 in zip(lst1, lst2):
#     print (x1, x2)
#     res.append(x1+x2)

# res = [x1 + x2 for x1,x2 in zip(lst1,lst2)]
for i in range(min(len(lst1), len(lst2))):
    res.append(lst1[i] + lst2[i])

print(res)


