# Task 1: Create a list of numbers and use pop() to remove the last two items

numbers = [10, 20, 30, 40, 50, 60]

numbers.pop()   # removes last item
numbers.pop()   # removes second last item

print("Task 1 Output:", numbers)


# Task 2: Make a list of 5 countries. Use insert() to add one at index 3,
# then use count() to count a specific country

countries = ["Pakistan", "India", "China", "Turkey", "Japan"]

countries.insert(3, "Saudi Arabia")

count_country = countries.count("Pakistan")

print("Task 2 Output:", countries)
print("Count of Pakistan:", count_country)


# Task 3: Create a list of integers. Use sort() and then reverse()
# to show them in descending order

integers = [45, 12, 78, 23, 9, 56]

integers.sort()
integers.reverse()

print("Task 3 Output:", integers)


# Task 4: Use copy() to duplicate a list. Change one element in the copy
# and show that the original list remains unchanged

original_list = ["Ali", "Ahmed", "Sara", "Zain"]

copied_list = original_list.copy()

copied_list[1] = "Hassan"

print("Task 4 Original List:", original_list)
print("Task 4 Copied List:", copied_list)


# Task 5: Combine two lists of fruits and vegetables and check
# if 'apple' is present in the combined list

fruits = ["apple", "banana", "mango"]
vegetables = ["potato", "tomato", "onion"]

combined_list = fruits + vegetables

print("Task 5 Combined List:", combined_list)

if "apple" in combined_list:
    print("Apple is present in the combined list")
else:
    print("Apple is not present in the combined list")
