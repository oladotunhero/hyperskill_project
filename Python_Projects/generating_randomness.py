SAVED_INPUT = ""
while True:
    entry = input("Print a random string containing 0 or 1: ")
    numbers = entry.translate({ord(i): None for i in entry if i not in "01"})
    SAVED_INPUT += numbers
    numbers_left = 100 - len(SAVED_INPUT)
    if len(SAVED_INPUT) >= 100:
        break
    else:
        print(f"Current data length is {len(SAVED_INPUT)}, {numbers_left} symbols left")
print(f"Final data string:\n{SAVED_INPUT}")

triads = ['000', '001', '010', '011', '100', '101', '110', '111']
counts = {triad: [0, 0] for triad in triads}

for i in range(len(SAVED_INPUT) - 3):
    triad = SAVED_INPUT[i:i+3]  
    next_char = SAVED_INPUT[i+3]  
    if triad in counts:
        digit = int(next_char)  
        counts[triad][digit] += 1  

# Print the results
for triad in triads:
    print(f"{triad}: {counts[triad][0]},{counts[triad][1]}")