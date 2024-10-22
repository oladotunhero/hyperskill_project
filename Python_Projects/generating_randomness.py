import random

display = '''Please provide AI some data to learn...
The current data length is 0, 100 symbols left'''
print(display)

SAVED_INPUT = ""
while True:
    entry = input("Print a random string containing 0 or 1: ")
    numbers = entry.translate({ord(i): None for i in entry if i not in "01"})
    SAVED_INPUT = SAVED_INPUT + numbers
    numbers_left = 100 - len(SAVED_INPUT)
    if len(SAVED_INPUT) >= 100:
        break
    else:
        print(f"The Current data length is {len(SAVED_INPUT)}, {numbers_left} symbols left")
print(f"Final data string:\n{SAVED_INPUT}")

triads = ['000', '001', '010', '011', '100', '101', '110', '111']

# Initialize counts for each triad as a list [count_of_0, count_of_1]
counts = {triad: [0, 0] for triad in triads}

# Iterate through SAVED_INPUT and update counts
for i in range(len(SAVED_INPUT) - 3):
    triad = SAVED_INPUT[i:i+3]  # Get the triad
    next_char = SAVED_INPUT[i+3]  # Get the character following the triad
    if triad in counts:
        digit = int(next_char)  # Convert next_char to integer 0 or 1
        counts[triad][digit] += 1  # Increment the count at index 0 or 1

# Print the results
for triad in triads:
    print(f"{triad}: {counts[triad][0]},{counts[triad][1]}")

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!""")

NEW_INPUT = ""
Cash = 1000
while True:
    new_entry = input("Print a random string containing 0 or 1: ")
    if new_entry == "enough":
        print("Game over!")
        break
    else:
        new_number = ''.join(filter(lambda x: x in '01', new_entry))
        if len(new_number) >= 4:
            NEW_INPUT = new_number
        else:
            print("This string is too short,enter at least four characters containing 0 or 1")
            continue

    predictions = ""
    for i in range(len(NEW_INPUT) - 3):
        triad = NEW_INPUT[i:i + 3]
        if triad in counts:
            count_0, count_1 = counts[triad]
            if count_0 > count_1:
                prediction = "0"
            elif count_1 > count_0:
                prediction = "1"
        else:
            prediction = str(random.randint(0, 1))
        predictions += prediction
    print(f"predictions:\n{predictions}")

    # calculate the accuracy
    actual = NEW_INPUT[3:]
    correct = 0
    for a, b in zip(actual, predictions):
        if a == b:
            correct += 1
    total = len(actual)
    accuracy = "{0:.2f}".format((correct / total) * 100)

    print(f"Computer guessed {correct} out of {total} symbols right ({accuracy}%)")

    wins = total - correct
    losses = correct
    Cash = Cash - losses + wins

    print(f"Your balance is now ${Cash}")

    for i in range(len(NEW_INPUT) - 3):
        triad = NEW_INPUT[i:i+3]
        next_char = NEW_INPUT[i + 3]
        if triad in counts:
            digit = int(next_char)
            counts[triad][digit] += 1