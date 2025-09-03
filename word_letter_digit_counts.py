numOfWords = 0
numOfLetters = 0
numOfDigits = 0
text = input("Enter the text:")
for i in text:
    i = i.lower()
    if i >= 'a' and i <= 'z':
        numOfWords = numOfWords + 1
    elif i >= '0' and i<='9':
        numOfDigits = numOfDigits+1
    elif i == ' ':
        numOfLetters = numOfLetters + 1
print("Number of Words = ",numOfWords )
print("Number of Digits = ",numOfDigits)
print("Number of Letters = ", numOfLetters)