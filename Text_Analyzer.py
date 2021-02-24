# Prewritten texts and users
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
USERS = """
| USER |   PASSWORD  |
-----------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |
"""

# Sign in
print(60*"-")
username_input = input(f"Hello,\nhere are prewriten users for testing:{USERS}\nEnter your username: " )
password_input = input("And now,\nenter your password please : ")

sign_in_list = list((username_input, password_input))
sign_in_data = [["bob", "123"], ["ann", "pass123"], ["mike", "password123"], ["mike", "password123"], ["liz", "pass123"]]

if sign_in_list in sign_in_data:
    print(60* "-")
    print(f"\nWelcome to the Text Analyzer, {username_input}.")

else:
    print(60 * "-")
    print("Ooops. You have entered wrong username or wrong password.")
    exit()

# An offer
print("We have three texts to by analyzed. You can choose one.")
input("Press enter to continue.")

print(f"\nText number (1) is:{TEXTS[0]}")
input("Press enter to continue.")

print(f"\nText number (2) is:\n{TEXTS[1]}")
input("Press enter to continue.")

print(f"\nText number (3) is:\n{TEXTS[2]}\n")
print(60 * "-")

# A selection
selection = int(input("Make your selection by writting number of chosen text: "))

if selection not in [1, 2, 3]:
    print("You have entered wrong input.")
    exit()

# Text to clean words
selected_text_list = TEXTS[selection - 1].strip().split(" ")
words_of_selected_text = []

for word in selected_text_list:
    words_of_selected_text.append(word.strip(",.\n"))
 
# Word counter
number_of_words = len(words_of_selected_text)

# Words with first character big
first_upper = 0
for word in words_of_selected_text:
    if word[0].isupper():
        first_upper += 1


# Words with all upper characters
all_upper = 0
for word in words_of_selected_text:
    if word.isupper() and word.isalpha():
        all_upper += 1

# Words with all lower charracters
all_lower = 0
for word in words_of_selected_text:
    if word.islower():
        all_lower += 1

# Number of numbers
numbers = 0
for number in words_of_selected_text:
    if number.isnumeric():
        numbers += 1
# Sum of numbers
sum_of_numbers = 0
for number in words_of_selected_text:
    if number.isnumeric():
        sum_of_numbers += int(number)

# Lenght counter

# Print all
print(60 * "-")
if number_of_words == 0:
    print("There are no words in the text.")
elif number_of_words == 1:
    print(f"There is {number_of_words} in the text.")
else:
    print(f"There are {number_of_words} words in the text.")

if first_upper == 0:
    print("There are no titlecase words in the text.")
elif first_upper == 1:
    print(f"There is {first_upper} titlecase word in the text.")
else:
    print(f"There are {first_upper} titlecase words in the text.")

if all_upper == 0:
    print("There are no uppercase words in the text.")
elif all_upper == 1:
    print(f"There is {all_upper} uppercase word in the text.")
else:
    print(f"There are {all_upper} uppercase words in the text.")

if all_lower == 0:
    print("There are no lowercase words in the text.")
elif all_upper == 1:
    print(f"There is {all_lower} lowercase word in the text.")
else:
    print(f"There are {all_lower} lowercase words in the text.")

if numbers == 0:
    print("There are no numbers in the text.")
elif numbers == 1:
    print(f"There is {numbers} number in the text.")
else:
    print(f"There are {numbers} numeric strings in the text.")

if sum_of_numbers == 0:
    print("There are no numbers in the text.")
else:
    print(f"The sum of all numbers is {sum_of_numbers}.")

# Occurrences
occurences = []

for word in words_of_selected_text:
    occurences.append(len(word))

lenghts = list(set(occurences))

# Print graph
print(60 * "-")
print("LEN | OCCURENCES | NR.")
for lenght in lenghts:
    print(lenght, "|",  occurences.count(lenght) * "*", "|", occurences.count(lenght))
print(60 * "-")
