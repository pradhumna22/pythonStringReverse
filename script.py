
reverseString = input("Please enter a string to be reversed: ")

for i in range(len(reverseString)):
        counter = len(reverseString) - i -1
        print(reverseString[counter], end ="")