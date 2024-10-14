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
