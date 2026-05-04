# Problem 01: The Word Energy Calculator (5 marks) - CLO1
# Write a Python function named calculate_word_energy that takes your favorite word as input and analyzes it based on two properties:
# Check if the word contains more vowels than consonants.


# Check if the word length is a multiple of 3.


# Based on these two properties, print different outputs:


# Conditions and Outputs:
# If the word has more vowels than consonants, print:  "Your word is full of energy!"
# If the word has more consonants and its length is a multiple of 3, print:  "Your word has a strong and balanced form."
# If the word has more consonants and its length is NOT a multiple of 3, print: "Your word is strong but not perfectly balanced."
# Example:
# Input: "Amazing" , Output: Your word is full of energy!
# Input: "strength", Output: Your word has a strong but not perfectly balanced form

# Problem 01: Word Energy Calculator
def calculate_word_energy(word):
    vowels = "aeiouAEIOU"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha():  # ignore non-letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    length = len(word)

    # Conditions
    if vowel_count > consonant_count:
        print("Your word is full of energy!")
    elif consonant_count > vowel_count and length % 3 == 0:
        print("Your word has a strong and balanced form.")
    else:
        print("Your word is strong but not perfectly balanced.")

# Problem 02: The Food Supply Manager (5 marks) - CLO1

# A disaster relief center has 2 food storage units (Storage A and Storage B) and 3 shelters (Shelter 1, Shelter 2, Shelter 3) that need food supplies.
# Each storage unit has a maximum capacity (in food packets) and  current food packet count.
# Each shelter Needs a specific number of food packets.
# Write a Python program that:
# Stores the current food packet levels of Storage A and Storage B.


# Stores the food packet needs of Shelter 1, Shelter 2, and Shelter 3.


# You can start with any storage unit to distribute the food.


# After distribution, your program must:


# Print how many packets each shelter received.


# Print how many packets remain in each storage unit.


# If any shelter's full need could not be met, print a warning message.


# Example:
# Suppose:
# Storage A: 400 packets, Storage B: 250 packets


# Shelter 1 needs 150 packets, Shelter 2 needs 300 packets, Shelter 3 needs 100 packets


# Your program may allocate:
# 150 packets from Storage A to Shelter 1 (Storage A now has 250 packets left).


# 250 packets from Storage A to Shelter 2 (Storage A now has 0 packets left).


# 50 packets from Storage B to Shelter 2 (Storage B now has 200 packets left).


# 100 packets from Storage B to Shelter 3 (Storage B now has 100 packets left).
 # Storage food packets
storage_A = 400
storage_B = 250

# Shelter needs
shelter1_need = 150
shelter2_need = 300
shelter3_need = 100

# Track received food
s1_received = 0
s2_received = 0
s3_received = 0

# Function to distribute food
def distribute(storage, need):
    given = min(storage, need)
    storage -= given
    need -= given
    return storage, need, given


# ---- Distribution starts ----

# Shelter 1
storage_A, shelter1_need, s1_received = distribute(storage_A, shelter1_need)

# Shelter 2
storage_A, shelter2_need, temp = distribute(storage_A, shelter2_need)
s2_received += temp

storage_B, shelter2_need, temp = distribute(storage_B, shelter2_need)
s2_received += temp

# Shelter 3
storage_B, shelter3_need, s3_received = distribute(storage_B, shelter3_need)


# ---- Output ----
print("Food Distribution Summary:")
print("Shelter 1 received:", s1_received)
print("Shelter 2 received:", s2_received)
print("Shelter 3 received:", s3_received)

print("\nRemaining Food:")
print("Storage A:", storage_A)
print("Storage B:", storage_B)

# Warning messages
if shelter1_need > 0:
    print("Warning: Shelter 1 did not receive full supply!")
if shelter2_need > 0:
    print("Warning: Shelter 2 did not receive full supply!")
if shelter3_need > 0:
    print("Warning: Shelter 3 did not receive full supply!")