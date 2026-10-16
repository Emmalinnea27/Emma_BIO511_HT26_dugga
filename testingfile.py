## Note: commenting this code in a way that highlights my knowledge of python, why and how things function the way they do, and how I am implementing as a result
## Comments not to be interpreted as pseudocode (I know they are far too long), rather as evidence of my full understanding of this Python Module
## Thank You :)


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

# Implementing fstrings throughout to increase user readability in the output terminal... That way it doesn't just spit out info, rather attaches meaning to it when we are printing lots of different things
cleaned_my_list = clean_list(my_list)
print(f"Cleaned list: {cleaned_my_list}")


# Part 2 - C
# We want to calculate the sum of the neighbors in the new_list. Start by creating a summed_list list-type variable to store our new information

summed_list = []

# Iterate through the list using range (walks through the length of the list)
# Included -1 because we need to be careful when considering lengths. Positioning starts at 0, 1, 2... etc. This will take us to the end of the list and consider each item

for j in range(len(new_list) - 1):
    summed_list.append(new_list[j] + new_list[j+1])

print(f"Summed list: {summed_list}")






## QUESTION 3

# Question 3 - A
import pandas as pd

# Reading in the information, and printing a few lines so I can see what I'm working with as well as get a column review!
df = pd.read_csv('cnv_data.csv', sep=r'\s+')
print(df.columns)
print (df.head(8))


# We need to make a scatterplot of the data in the dataframe. We will use seaborn and matplotlib for this. 
# Start by importing all the necesary libraries (we will use seaborn and matplotlib)
# Note that we change the names to sns and plt so that they are easier to call as we will use them several times in the remainder of our code
import seaborn as sns
import matplotlib.pyplot as plt

# Assigning values for the x and y axes
sns.scatterplot(
    data=df,
    x="position_mb",
    y="log2_ratio",
)

# Question 3 - B
# Showing and saving the plot as a png for easy access later!
# Also adding "pretty" titles and names for best user readability
plt.xlabel("Genomic Position (Mb)")
plt.ylabel("Log2 Ratio")
plt.title("Copy Number Variation Across Genomic Positions")
plt.savefig('cnv_scatterplot.png')
plt.show()

##  note that I used AI in part A of this question. I wrote the code to generate the scatterplot, but was unable to access the image due to an error.
## All of the code is my own, with the exception of the 'sep=r'\s+'' separation designation, which allowed the code to understand how the csv file was truly separated


# Question 3 - C
# Please see the SEPARATE file: Question3PartC.py for this part. 

# Selected to separate this question/response only because the input/output files are not "real" at this time


## QUESTION 4
# Question 4 - A

# Outcomes: Win, Loss, Draw
# We will use a dictionary to store the outcomes and their counts...
# Keys: Game number (1-20)
# Values: Game result (Alice wins, Bob wins, Draw)

import random
random.randint(1, 6) # generates a random integer between 1 and 6 (inclusive)

# Starting by creating an empty dictionary we will store the results in
gameresults = {}

for game in range (20):
    alice = random.randint(1, 6)
    bob = random.randint(1, 6)

    if alice > bob:
        gameresults[game + 1] = "Alice wins"
    elif bob > alice:
        gameresults[game + 1] = "Bob wins"
    else:
        gameresults[game + 1] = "Draw"

print (gameresults)
print (f"Alice won {list(gameresults.values()).count('Alice wins')} times.")
print (f"Bob won {list(gameresults.values()).count('Bob wins')} times.")
print (f"Draws: {list(gameresults.values()).count('Draw')} times.")


# A little extra here (not required for the dugga) but I wanted to print the overall winner.
# This will compare the counts of Alice to Bob wins and print the overall winner, accounting for draws as well
# Lots of print statements here for user readability/understanding, but could absolutely be condensed

if list(gameresults.values()).count('Alice wins') > list(gameresults.values()).count('Bob wins'):
    print ("Alice is the overall winner!")
elif list(gameresults.values()).count('Bob wins') > list(gameresults.values()).count('Alice wins'):
    print ("Bob is the overall winner!")
else:
    print ("The overall result is a draw!")



# Question 4 - B
# Improving my code by adding a loop into the function. 

# Takes input for players 1 and 2
user1 = input ("Enter Player 1's Name: ")
user2 = input ("Enter Player 2's Name: ")

# Takes input for how many games should be played
numgames = int(input("How many rounds should be played: "))

# Now inputting the loop into a function that can be called and executed several times

def new_game (player1, player2, gamecount):
    ourgameresults = {}

    for game in range(gamecount):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        if dice1 > dice2:
            ourgameresults[game + 1] = player1
        elif dice2 > dice1:
            ourgameresults[game + 1] = player2
        else:
            ourgameresults[game + 1] = "Draw"
    # Be sure to return dictionary to output!
    return ourgameresults

#Calling our (updated) function new_game here. Using our user input (aka user1, user2, numgames) as the inputs for this function.
#This line ultimately prints the entirety of the newly created dictionary.
print(new_game(user1, user2, numgames))
