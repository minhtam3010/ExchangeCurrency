f = open("./AmountATM/unitOfMoneyATM1.txt")
res = dict()
for each in f:
    print(each[:-1], end=" ")
    split_arr = each[:-1].split(":")
    print(split_arr)
    res[split_arr[0]] = int(split_arr[1])

print(res)

# f = open("./test.txt", "a+")
# f.seek(0)
# f.truncate()


# f = open("./AmountATM/ATM1.txt", "a+")
# f.seek(0)
# res = []
# for each in f:
#     if "\n" in each:
#         res.append(each[:len(each) - 1])
#     else:
#         res.append(each[15:])
# print(res)