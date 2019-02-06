def funcname(*parameter_list):
    print(*parameter_list)


def funcname2(*parameter_list):
    print(parameter_list)


funcname(1, 2, 3)
print(1, 2, 3)

funcname2(1, 2, 3)
print((1, 2, 3))
