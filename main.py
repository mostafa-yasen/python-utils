# Get a list of inputes separated by space
# arr = list(map(int,input().split()))
# print("Input List:",arr)


# Get a variable size in memory
# import sys

# x = 120
# print(sys.getsizeof(x))


# get the uid of a variable
# y = "A variable"
# print(id(y))

# Check for an Anagram
# def check_anagram(args):
#     if not args:
#         return False

#     first_arg = sorted(args.pop())
#     for arg in args:
#         if first_arg != sorted(arg):
#             return False

#     return True

# args = list(map(str, input().split()))
# print(check_anagram(args))

# Get the most frequent in a list
# def most_frequent(lst):
#     return None if not lst else max(set(lst), key=lst.count)

# out = most_frequent(['mostafa', 'ahmed', 'yasin', 'mohamed', 'hassan', 'yasin'])
# out = most_frequent([])
# print(out)

# Finding duplicates
# def has_duplicates(lst):
#     return len(lst) != len(set(lst))
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5, 3]
# print(has_duplicates(x))
# print(has_duplicates(y))

# Swap Values
# def swap(x, y):
#     return y, x

# x, y = 'x', 'y'
# print(swap(x, y))


# Calculator
# import operator

# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
#     "**": operator.pow
# }
# print(actions["**"](2, 5))


# Calculating Time of a Shell
# import datetime
# start = datetime.datetime.now()
# lst = sorted([5,6,8,45,1,2,5,6,3,1,4,7,8,5,9,6,3,2,1,4,4,55,4,122,8,55,2])
# print(lst)
# print(f"list sorted in {datetime.datetime.now() - start}")
