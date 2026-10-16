# PART 1- A
# This variable type is a string, strings are immutable. Contains letter information (like my name)
my_name  = "emma"
print(my_name)


# PART 1- B
# Len function is used to get the length of a string. Counts the characters in my_name variable.
name_length = len(my_name)
print(name_length)
# We can also use an fstring to print the length of the string in a more readable format.
print(f"The length of my name is: {name_length}")


# PART 1- C
# the letter m occurs in my name (twice). Let's print the number of times it occurs...
# Note that changing the letter and keeping the rest of the code the same will still produce the right print output and correct answer!
counter = 0
for letter in my_name:
    if letter == "m":
        counter += 1
print(f"The letter {letter} occurs in my name: {counter} times")




# QUESTION 2

my_list = [1, 5, "4", "six", 3.14]
# In my_list, we have 5 elements of different types: integers, strings, and a float. The list is mutable, meaning we can change its contents after creation.
print(my_list)

# Part 2 - A
# We want to loop through my_list and convert each item to an int and add to a new_list.
# We will have some failures, because some items cannot be converted to int (like "six" and 3.14). We will use a try/except block to handle these cases. This means we need to use try/except logic within our loop
# Thus... use a for loop to iterate through my_list and use a ValueError to catch the values that we cannot swap over to an int type!
new_list = []
for item in my_list:
    try:
        new_list.append(int(item))
    except ValueError:
        print(f"Cannot convert {item} to int.")
print (f"Our new list is: {new_list}")

# Part 2 - B
# We want to create a function called clean_list that takes a list as input and returns a new list with only the items that can be converted to int. We will use the same try/except logic as before, but this time we will encapsulate it in a function.
def clean_list(input_list):
    cleaned_list = []
    for item in input_list:
        try:
            cleaned_list.append(int(item))
        except ValueError:
            print(f"Cannot convert {item} to int.")
    return cleaned_list

cleaned_my_list = clean_list(my_list)
print(f"Cleaned list: {cleaned_my_list}")


# Part 2 - C
# We want to calculate the sum of the neighbors in the new_list.
# DONT FORGET TO SWAP THIS TO CLEANED_MY_LIST WHEN YOU ARE DONE TESTING!
summed_list = []

for j in range(len(new_list) - 1):
    summed_list.append(new_list[j] + new_list[j+1])

print(f"Summed list: {summed_list}")



## QUESTION 3

