# an_int = 4
# b_int = an_int
# a_bool = False
# write a program to show the type and the memory address of a variable
# value
# print(type(a_bool))
# print(id(a_bool))
# print(id(an_int), id(b_int))
###### write a code to declare an array and its corresponding
# location in the RAM
# a_list = [1, 2, 3]
# print(id(a_list), id(a_list[2]))
# an_int = 4
# b_int = 4
# print(id(an_int), id(b_int))
# a = [1, 2, 3]
# print(id(a), id(a[2]))
# a[2] = 4
# print(id(a[2]))
# A = (1, 2, 3)
# print(id(A), id(A[2]))
# A[2] = 4
B = (1, 2, [4, 5, 6])
print(id(B), id(B[2]), id(B[2][2]))
B[2][2] = 7
print(id(B), id(B[2]), id(B[2][2]))
