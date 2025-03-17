a = input("Enter an input: ")
b = int(a)

my_list = ["a", "b", "c", "d", "e"]

my_list.__setitem__(1, "z")
my_list.__getitem__(1)
print(my_list)