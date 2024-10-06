the_list = [4, 3, 6, 9, 1, 7]
target = 6

the_list.sort()  # Sort the list before searching
print(the_list)  # [1, 3, 4, 6, 7, 9]

def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot -1
        else:
            lower_bound = pivot +1

    return -1

result = binary_search(the_list, target)
print(result)  # 0
print(binary_search(the_list, 5))